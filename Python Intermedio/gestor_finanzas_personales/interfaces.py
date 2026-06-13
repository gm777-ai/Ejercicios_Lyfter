from __future__ import annotations

from pathlib import Path

try:
    import PySimpleGUI as sg
except ModuleNotFoundError:
    import FreeSimpleGUI as sg

from logica import (
    COLOR_DEFECTO,
    TIPO_GASTO,
    TIPO_INGRESO,
    GestorFinanzas,
    Movimiento,
    fecha_hoy_texto,
)
from persistencia import cargar_datos, exportar_movimientos_csv, guardar_datos

ENCABEZADOS_TABLA = ["Fecha", "Título", "Monto", "Categoría", "Tipo"]


def ejecutar_app() -> None:
    sg.theme("LightBlue2")
    gestor = cargar_datos()
    movimientos_visibles = gestor.movimientos.copy()

    window = crear_ventana_principal(gestor, movimientos_visibles)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Salir"):
            guardar_datos(gestor)
            break

        if event == "Agregar categoría":
            agregar_categoria_desde_gui(gestor)
            guardar_datos(gestor)
            movimientos_visibles = gestor.movimientos.copy()
            actualizar_ventana_principal(window, gestor, movimientos_visibles)

        elif event == "Agregar gasto":
            agregar_movimiento_desde_gui(gestor, TIPO_GASTO)
            guardar_datos(gestor)
            movimientos_visibles = gestor.movimientos.copy()
            actualizar_ventana_principal(window, gestor, movimientos_visibles)

        elif event == "Agregar ingreso":
            agregar_movimiento_desde_gui(gestor, TIPO_INGRESO)
            guardar_datos(gestor)
            movimientos_visibles = gestor.movimientos.copy()
            actualizar_ventana_principal(window, gestor, movimientos_visibles)

        elif event == "Filtrar":
            try:
                movimientos_visibles = gestor.filtrar_movimientos_por_fecha(
                    values["-FECHA-INICIO-"],
                    values["-FECHA-FIN-"],
                )
                actualizar_ventana_principal(window, gestor, movimientos_visibles)
            except ValueError as error:
                sg.popup_error(str(error), title="Error de validación")

        elif event == "Limpiar filtro":
            movimientos_visibles = gestor.movimientos.copy()
            window["-FECHA-INICIO-"].update("")
            window["-FECHA-FIN-"].update("")
            actualizar_ventana_principal(window, gestor, movimientos_visibles)

        elif event == "Exportar a CSV":
            exportar_csv_desde_gui(gestor)

    window.close()


def crear_ventana_principal(gestor: GestorFinanzas, movimientos: list[Movimiento]) -> sg.Window:
    filas_tabla = convertir_movimientos_a_filas(movimientos)
    colores_filas = obtener_colores_filas(gestor, movimientos)
    totales = gestor.calcular_totales(movimientos)

    layout = [
        [sg.Text("Gestor de Finanzas Personales", font=("Arial", 18, "bold"))],
        [
            sg.Button("Agregar categoría"),
            sg.Button("Agregar gasto"),
            sg.Button("Agregar ingreso"),
            sg.Button("Exportar a CSV"),
            sg.Button("Salir"),
        ],
        [
            sg.Text("Fecha inicio:"),
            sg.Input(key="-FECHA-INICIO-", size=(12, 1), tooltip="Formato: dd/mm/yyyy"),
            sg.Text("Fecha fin:"),
            sg.Input(key="-FECHA-FIN-", size=(12, 1), tooltip="Formato: dd/mm/yyyy"),
            sg.Button("Filtrar"),
            sg.Button("Limpiar filtro"),
        ],
        [
            sg.Table(
                values=filas_tabla,
                headings=ENCABEZADOS_TABLA,
                key="-TABLA-",
                row_colors=colores_filas,
                auto_size_columns=False,
                col_widths=[12, 28, 12, 18, 10],
                justification="left",
                num_rows=14,
                expand_x=True,
                expand_y=True,
            )
        ],
        [
            sg.Text(f"Ingresos: ${totales['ingresos']:.2f}", key="-TOTAL-INGRESOS-", size=(22, 1)),
            sg.Text(f"Gastos: ${totales['gastos']:.2f}", key="-TOTAL-GASTOS-", size=(22, 1)),
            sg.Text(f"Balance neto: ${totales['balance_neto']:.2f}", key="-TOTAL-BALANCE-", size=(24, 1)),
        ],
    ]

    return sg.Window("Gestor de Finanzas Personales", layout, finalize=True, resizable=True)


def agregar_categoria_desde_gui(gestor: GestorFinanzas) -> None:
    layout = [
        [sg.Text("Nombre de la categoría:"), sg.Input(key="-NOMBRE-", size=(30, 1))],
        [
            sg.Text("Color:"),
            sg.Input(default_text=COLOR_DEFECTO, key="-COLOR-", size=(12, 1)),
            sg.ColorChooserButton("Elegir color", target="-COLOR-"),
        ],
        [sg.Button("Guardar"), sg.Button("Cancelar")],
    ]

    window = sg.Window("Agregar categoría", layout, modal=True)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Cancelar"):
            break

        if event == "Guardar":
            try:
                categoria = gestor.agregar_categoria(values["-NOMBRE-"], values["-COLOR-"])
                sg.popup_ok(f"Categoría agregada: {categoria.nombre}", title="Éxito")
                break
            except ValueError as error:
                sg.popup_error(str(error), title="Error de validación")

    window.close()


def agregar_movimiento_desde_gui(gestor: GestorFinanzas, tipo: str) -> None:
    if not gestor.categorias:
        sg.popup_error(
            "Debe agregar al menos una categoría antes de registrar ingresos o gastos.",
            title="Categorías requeridas",
        )
        return

    layout = [
        [sg.Text("Título:"), sg.Input(key="-TITULO-", size=(35, 1))],
        [sg.Text("Monto:"), sg.Input(key="-MONTO-", size=(15, 1))],
        [sg.Text("Categoría:"), sg.Combo(gestor.obtener_nombres_categorias(), key="-CATEGORIA-", readonly=True, size=(25, 1))],
        [sg.Text("Fecha:"), sg.Input(default_text=fecha_hoy_texto(), key="-FECHA-", size=(12, 1)), sg.Text("dd/mm/yyyy")],
        [sg.Button("Guardar"), sg.Button("Cancelar")],
    ]

    window = sg.Window(f"Agregar {tipo.lower()}", layout, modal=True)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Cancelar"):
            break

        if event == "Guardar":
            try:
                movimiento = gestor.agregar_movimiento(
                    titulo=values["-TITULO-"],
                    monto=values["-MONTO-"],
                    categoria=values["-CATEGORIA-"],
                    tipo=tipo,
                    fecha=values["-FECHA-"],
                )
                sg.popup_ok(
                    f"Nuevo {tipo.lower()} agregado:\n"
                    f"Fecha: {movimiento.fecha} | Título: {movimiento.titulo} | "
                    f"Monto: ${movimiento.monto:.2f} | Tipo: {movimiento.tipo}",
                    title="Éxito",
                )
                break
            except ValueError as error:
                sg.popup_error(str(error), title="Error de validación")

    window.close()


def exportar_csv_desde_gui(gestor: GestorFinanzas) -> None:
    if not gestor.movimientos:
        sg.popup_error("No hay movimientos para exportar.", title="Sin datos")
        return

    ruta_archivo = sg.popup_get_file(
        "Guardar archivo CSV",
        save_as=True,
        default_extension=".csv",
        file_types=(("Archivos CSV", "*.csv"),),
        default_path="movimientos_exportados.csv",
    )

    if not ruta_archivo:
        return

    try:
        ruta_generada = exportar_movimientos_csv(gestor, Path(ruta_archivo))
        sg.popup_ok(f"Archivo CSV generado:\n{ruta_generada}", title="Exportación completa")
    except OSError as error:
        sg.popup_error(f"No se pudo exportar el archivo: {error}", title="Error")


def actualizar_ventana_principal(window: sg.Window, gestor: GestorFinanzas, movimientos: list[Movimiento]) -> None:
    filas_tabla = convertir_movimientos_a_filas(movimientos)
    colores_filas = obtener_colores_filas(gestor, movimientos)
    totales = gestor.calcular_totales(movimientos)

    window["-TABLA-"].update(values=filas_tabla, row_colors=colores_filas)
    window["-TOTAL-INGRESOS-"].update(f"Ingresos: ${totales['ingresos']:.2f}")
    window["-TOTAL-GASTOS-"].update(f"Gastos: ${totales['gastos']:.2f}")
    window["-TOTAL-BALANCE-"].update(f"Balance neto: ${totales['balance_neto']:.2f}")


def convertir_movimientos_a_filas(movimientos: list[Movimiento]) -> list[list[str]]:
    return [
        [
            movimiento.fecha,
            movimiento.titulo,
            f"${movimiento.monto:.2f}",
            movimiento.categoria,
            movimiento.tipo,
        ]
        for movimiento in movimientos
    ]


def obtener_colores_filas(gestor: GestorFinanzas, movimientos: list[Movimiento]) -> list[tuple[int, str, str]]:
    colores = []

    for indice, movimiento in enumerate(movimientos):
        categoria = gestor.buscar_categoria(movimiento.categoria)
        if categoria is None:
            continue

        color_fondo = categoria.color
        color_texto = obtener_color_texto_contraste(color_fondo)
        colores.append((indice, color_texto, color_fondo))

    return colores


def obtener_color_texto_contraste(color_hex: str) -> str:
    color = color_hex.lstrip("#")
    rojo = int(color[0:2], 16)
    verde = int(color[2:4], 16)
    azul = int(color[4:6], 16)
    brillo = (rojo * 299 + verde * 587 + azul * 114) / 1000
    return "black" if brillo > 140 else "white"
