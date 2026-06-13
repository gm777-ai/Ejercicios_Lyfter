from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Optional

from logica import GestorFinanzas

CARPETA_DATOS = Path("datos")
ARCHIVO_DATOS = CARPETA_DATOS / "finanzas.json"


def cargar_datos(ruta_archivo: Optional[Path] = None) -> GestorFinanzas:
    ruta = ruta_archivo or ARCHIVO_DATOS

    if not ruta.exists():
        return GestorFinanzas()

    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            data = json.load(archivo)
        return GestorFinanzas.from_dict(data)
    except (json.JSONDecodeError, KeyError, TypeError, ValueError):
        return GestorFinanzas()


def guardar_datos(gestor: GestorFinanzas, ruta_archivo: Optional[Path] = None) -> None:
    ruta = ruta_archivo or ARCHIVO_DATOS
    ruta.parent.mkdir(parents=True, exist_ok=True)

    with ruta.open("w", encoding="utf-8") as archivo:
        json.dump(gestor.to_dict(), archivo, indent=4, ensure_ascii=False)


def exportar_movimientos_csv(gestor: GestorFinanzas, ruta_csv: Path | str) -> Path:
    ruta = Path(ruta_csv)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    totales = gestor.calcular_totales()

    with ruta.open("w", newline="", encoding="utf-8-sig") as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(["Fecha", "Título", "Monto", "Categoría", "Tipo"])

        for movimiento in gestor.movimientos:
            writer.writerow([
                movimiento.fecha,
                movimiento.titulo,
                f"{movimiento.monto:.2f}",
                movimiento.categoria,
                movimiento.tipo,
            ])

        writer.writerow([])
        writer.writerow(["Totales:"])
        writer.writerow(["Ingresos:", f"${totales['ingresos']:.2f}"])
        writer.writerow(["Gastos:", f"${totales['gastos']:.2f}"])
        writer.writerow(["Balance Neto:", f"${totales['balance_neto']:.2f}"])

    return ruta
