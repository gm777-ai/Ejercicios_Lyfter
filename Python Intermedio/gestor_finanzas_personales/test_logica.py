import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path

from logica import (
    TIPO_GASTO,
    TIPO_INGRESO,
    GestorFinanzas,
    fecha_hoy_texto,
    formatear_fecha,
    validar_color_hex,
    validar_monto_positivo,
)
from persistencia import cargar_datos, exportar_movimientos_csv, guardar_datos


class TestGestorFinanzas(unittest.TestCase):
    def crear_gestor_con_categoria(self):
        gestor = GestorFinanzas()
        gestor.agregar_categoria("Comida", "#FFA500")
        return gestor

    def test_agregar_categoria_correctamente(self):
        gestor = GestorFinanzas()
        categoria = gestor.agregar_categoria("Trabajo", "#00FF00")
        self.assertEqual(categoria.nombre, "Trabajo")
        self.assertEqual(categoria.color, "#00FF00")
        self.assertEqual(len(gestor.categorias), 1)

    def test_no_permite_categoria_vacia(self):
        gestor = GestorFinanzas()
        with self.assertRaises(ValueError):
            gestor.agregar_categoria("   ")

    def test_no_permite_categoria_duplicada(self):
        gestor = GestorFinanzas()
        gestor.agregar_categoria("Comida")
        with self.assertRaises(ValueError):
            gestor.agregar_categoria(" comida ")

    def test_no_permite_movimiento_sin_categorias(self):
        gestor = GestorFinanzas()
        with self.assertRaises(ValueError):
            gestor.agregar_movimiento("Salario", 1000, "Trabajo", TIPO_INGRESO, fecha_hoy_texto())

    def test_agregar_ingreso_guarda_monto_positivo(self):
        gestor = self.crear_gestor_con_categoria()
        movimiento = gestor.agregar_movimiento("Venta", 50, "Comida", TIPO_INGRESO, fecha_hoy_texto())
        self.assertEqual(movimiento.monto, 50)
        self.assertEqual(movimiento.tipo, TIPO_INGRESO)

    def test_agregar_gasto_guarda_monto_negativo(self):
        gestor = self.crear_gestor_con_categoria()
        movimiento = gestor.agregar_movimiento("Pizza", 40, "Comida", TIPO_GASTO, fecha_hoy_texto())
        self.assertEqual(movimiento.monto, -40)
        self.assertEqual(movimiento.tipo, TIPO_GASTO)

    def test_no_permite_monto_cero_o_negativo(self):
        with self.assertRaises(ValueError):
            validar_monto_positivo(0)
        with self.assertRaises(ValueError):
            validar_monto_positivo(-10)

    def test_no_permite_fecha_con_formato_incorrecto(self):
        gestor = self.crear_gestor_con_categoria()
        with self.assertRaises(ValueError):
            gestor.agregar_movimiento("Pizza", 40, "Comida", TIPO_GASTO, "2025/07/03")

    def test_no_permite_fecha_futura(self):
        gestor = self.crear_gestor_con_categoria()
        manana = formatear_fecha(date.today() + timedelta(days=1))
        with self.assertRaises(ValueError):
            gestor.agregar_movimiento("Pizza", 40, "Comida", TIPO_GASTO, manana)

    def test_filtrar_movimientos_por_rango_de_fechas(self):
        gestor = self.crear_gestor_con_categoria()
        gestor.agregar_movimiento("Movimiento viejo", 10, "Comida", TIPO_GASTO, "01/01/2024")
        gestor.agregar_movimiento("Movimiento nuevo", 20, "Comida", TIPO_GASTO, fecha_hoy_texto())

        resultado = gestor.filtrar_movimientos_por_fecha("01/01/2024", "31/12/2024")

        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0].titulo, "Movimiento viejo")

    def test_calcular_totales(self):
        gestor = self.crear_gestor_con_categoria()
        gestor.agregar_categoria("Trabajo", "#00FF00")
        gestor.agregar_movimiento("Salario", 1000, "Trabajo", TIPO_INGRESO, fecha_hoy_texto())
        gestor.agregar_movimiento("Comida", 100, "Comida", TIPO_GASTO, fecha_hoy_texto())

        totales = gestor.calcular_totales()

        self.assertEqual(totales["ingresos"], 1000)
        self.assertEqual(totales["gastos"], 100)
        self.assertEqual(totales["balance_neto"], 900)

    def test_valida_color_hex(self):
        self.assertEqual(validar_color_hex("#ffa500"), "#FFA500")
        with self.assertRaises(ValueError):
            validar_color_hex("orange")

    def test_guardar_y_cargar_datos(self):
        gestor = self.crear_gestor_con_categoria()
        gestor.agregar_movimiento("Pizza", 40, "Comida", TIPO_GASTO, fecha_hoy_texto())

        with tempfile.TemporaryDirectory() as carpeta_temporal:
            ruta = Path(carpeta_temporal) / "finanzas.json"
            guardar_datos(gestor, ruta)
            gestor_cargado = cargar_datos(ruta)

        self.assertEqual(len(gestor_cargado.categorias), 1)
        self.assertEqual(len(gestor_cargado.movimientos), 1)
        self.assertEqual(gestor_cargado.movimientos[0].titulo, "Pizza")

    def test_exportar_movimientos_csv(self):
        gestor = self.crear_gestor_con_categoria()
        gestor.agregar_movimiento("Pizza", 40, "Comida", TIPO_GASTO, fecha_hoy_texto())

        with tempfile.TemporaryDirectory() as carpeta_temporal:
            ruta = Path(carpeta_temporal) / "movimientos.csv"
            exportar_movimientos_csv(gestor, ruta)
            contenido = ruta.read_text(encoding="utf-8-sig")

        self.assertIn("Fecha,Título,Monto,Categoría,Tipo", contenido)
        self.assertIn("Pizza", contenido)
        self.assertIn("Balance Neto:", contenido)


if __name__ == "__main__":
    unittest.main()
