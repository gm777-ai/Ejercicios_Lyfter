from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
import re
from typing import Optional

FORMATO_FECHA = "%d/%m/%Y"
TIPO_INGRESO = "Ingreso"
TIPO_GASTO = "Gasto"
TIPOS_VALIDOS = {TIPO_INGRESO, TIPO_GASTO}
COLOR_DEFECTO = "#FFFFFF"


@dataclass
class Categoria:
    nombre: str
    color: str = COLOR_DEFECTO

    def __post_init__(self) -> None:
        self.nombre = validar_texto_no_vacio(self.nombre, "categoría")
        self.color = validar_color_hex(self.color)

    def to_dict(self) -> dict:
        return {"nombre": self.nombre, "color": self.color}

    @classmethod
    def from_dict(cls, data: dict) -> "Categoria":
        return cls(nombre=data["nombre"], color=data.get("color", COLOR_DEFECTO))


@dataclass
class Movimiento:
    titulo: str
    monto: float
    categoria: str
    tipo: str
    fecha: str

    def __post_init__(self) -> None:
        self.titulo = validar_texto_no_vacio(self.titulo, "título")
        self.categoria = validar_texto_no_vacio(self.categoria, "categoría")
        self.tipo = validar_tipo_movimiento(self.tipo)
        fecha_validada = validar_fecha_no_futura(self.fecha)
        self.fecha = formatear_fecha(fecha_validada)
        self.monto = float(self.monto)

    def to_dict(self) -> dict:
        return {
            "fecha": self.fecha,
            "titulo": self.titulo,
            "monto": self.monto,
            "categoria": self.categoria,
            "tipo": self.tipo,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Movimiento":
        return cls(
            titulo=data["titulo"],
            monto=float(data["monto"]),
            categoria=data["categoria"],
            tipo=data["tipo"],
            fecha=data["fecha"],
        )


class GestorFinanzas:
    def __init__(self, categorias: Optional[list[Categoria]] = None, movimientos: Optional[list[Movimiento]] = None):
        self.categorias: list[Categoria] = categorias or []
        self.movimientos: list[Movimiento] = movimientos or []

    def agregar_categoria(self, nombre: str, color: str = COLOR_DEFECTO) -> Categoria:
        nueva_categoria = Categoria(nombre=nombre, color=color)

        if self.buscar_categoria(nueva_categoria.nombre) is not None:
            raise ValueError("Ya existe una categoría con ese nombre")

        self.categorias.append(nueva_categoria)
        return nueva_categoria

    def buscar_categoria(self, nombre: str) -> Optional[Categoria]:
        nombre_normalizado = normalizar_nombre(nombre)
        for categoria in self.categorias:
            if normalizar_nombre(categoria.nombre) == nombre_normalizado:
                return categoria
        return None

    def obtener_nombres_categorias(self) -> list[str]:
        return [categoria.nombre for categoria in self.categorias]

    def agregar_movimiento(self, titulo: str, monto: str | float, categoria: str, tipo: str, fecha: str) -> Movimiento:
        if not self.categorias:
            raise ValueError("Debe agregar al menos una categoría antes de registrar ingresos o gastos")

        tipo_validado = validar_tipo_movimiento(tipo)
        categoria_encontrada = self.buscar_categoria(categoria)
        if categoria_encontrada is None:
            raise ValueError("La categoría seleccionada no existe")

        monto_validado = validar_monto_positivo(monto)
        if tipo_validado == TIPO_GASTO:
            monto_validado = -abs(monto_validado)
        else:
            monto_validado = abs(monto_validado)

        movimiento = Movimiento(
            titulo=titulo,
            monto=monto_validado,
            categoria=categoria_encontrada.nombre,
            tipo=tipo_validado,
            fecha=fecha,
        )
        self.movimientos.append(movimiento)
        return movimiento

    def filtrar_movimientos_por_fecha(self, fecha_inicio: str, fecha_fin: str) -> list[Movimiento]:
        inicio, fin = validar_rango_fechas(fecha_inicio, fecha_fin)

        movimientos_filtrados = []
        for movimiento in self.movimientos:
            fecha_movimiento = parsear_fecha(movimiento.fecha)
            if inicio <= fecha_movimiento <= fin:
                movimientos_filtrados.append(movimiento)

        return movimientos_filtrados

    def calcular_totales(self, movimientos: Optional[list[Movimiento]] = None) -> dict[str, float]:
        movimientos_a_calcular = movimientos if movimientos is not None else self.movimientos
        ingresos = sum(mov.monto for mov in movimientos_a_calcular if mov.tipo == TIPO_INGRESO)
        gastos = sum(abs(mov.monto) for mov in movimientos_a_calcular if mov.tipo == TIPO_GASTO)
        balance_neto = ingresos - gastos
        return {
            "ingresos": round(ingresos, 2),
            "gastos": round(gastos, 2),
            "balance_neto": round(balance_neto, 2),
        }

    def to_dict(self) -> dict:
        return {
            "categorias": [categoria.to_dict() for categoria in self.categorias],
            "movimientos": [movimiento.to_dict() for movimiento in self.movimientos],
        }

    @classmethod
    def from_dict(cls, data: dict) -> "GestorFinanzas":
        categorias = [Categoria.from_dict(item) for item in data.get("categorias", [])]
        movimientos = [Movimiento.from_dict(item) for item in data.get("movimientos", [])]
        return cls(categorias=categorias, movimientos=movimientos)


def normalizar_nombre(texto: str) -> str:
    return texto.strip().lower()


def validar_texto_no_vacio(texto: str, nombre_campo: str) -> str:
    texto_limpio = str(texto).strip()
    if not texto_limpio:
        raise ValueError(f"El campo {nombre_campo} no puede estar vacío")
    return texto_limpio


def validar_monto_positivo(monto: str | float) -> float:
    try:
        monto_convertido = float(str(monto).replace(",", "."))
    except ValueError as exc:
        raise ValueError("El monto debe ser un número válido") from exc

    if monto_convertido <= 0:
        raise ValueError("El monto debe ser mayor que cero")

    return round(monto_convertido, 2)


def validar_tipo_movimiento(tipo: str) -> str:
    tipo_limpio = str(tipo).strip().capitalize()
    if tipo_limpio not in TIPOS_VALIDOS:
        raise ValueError("El tipo de movimiento debe ser Ingreso o Gasto")
    return tipo_limpio


def parsear_fecha(fecha_texto: str) -> date:
    try:
        return datetime.strptime(str(fecha_texto).strip(), FORMATO_FECHA).date()
    except ValueError as exc:
        raise ValueError("Formato de fecha inválido (use dd/mm/yyyy)") from exc


def validar_fecha_no_futura(fecha_texto: str) -> date:
    fecha = parsear_fecha(fecha_texto)
    if fecha > date.today():
        raise ValueError("La fecha no puede ser en el futuro")
    return fecha


def validar_rango_fechas(fecha_inicio: str, fecha_fin: str) -> tuple[date, date]:
    inicio = validar_fecha_no_futura(fecha_inicio)
    fin = validar_fecha_no_futura(fecha_fin)

    if inicio > fin:
        raise ValueError("La fecha inicio no puede ser mayor que la fecha fin")

    return inicio, fin


def formatear_fecha(fecha: date) -> str:
    return fecha.strftime(FORMATO_FECHA)


def fecha_hoy_texto() -> str:
    return formatear_fecha(date.today())


def validar_color_hex(color: str) -> str:
    color_limpio = str(color).strip() if color else COLOR_DEFECTO
    if not color_limpio:
        color_limpio = COLOR_DEFECTO

    if not re.fullmatch(r"#[0-9a-fA-F]{6}", color_limpio):
        raise ValueError("El color debe tener formato hexadecimal, por ejemplo #FFA500")

    return color_limpio.upper()
