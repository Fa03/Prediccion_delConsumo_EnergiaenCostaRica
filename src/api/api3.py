
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse, HTMLResponse
import holidays
import locale
from datetime import datetime
from typing import Optional

# Se configura en español
try:
    locale.setlocale(locale.LC_TIME, "es_CR.UTF-8")
except locale.Error:
    locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")

app = FastAPI(title="API de Feriados CR", description="Devuelve feriados costarricenses en formato narrativo", version="1.0")

def obtener_feriados_narrativos(year: int, mes: Optional[int] = None,
                                 desde: Optional[str] = None,
                                 hasta: Optional[str] = None):
    feriados = holidays.CostaRica(years=year)
    lista = []

    fecha_desde = datetime.strptime(desde, "%Y-%m-%d").date() if desde else None
    fecha_hasta = datetime.strptime(hasta, "%Y-%m-%d").date() if hasta else None

    for fecha, nombre in sorted(feriados.items()):
        if mes and fecha.month != mes:
            continue
        if fecha_desde and fecha < fecha_desde:
            continue
        if fecha_hasta and fecha > fecha_hasta:
            continue

        dia_semana = fecha.strftime("%A").capitalize()
        dia = fecha.strftime("%d")
        mes_nombre = fecha.strftime("%B")
        año = fecha.strftime("%Y")

        descripcion = f"{dia_semana} {dia} de {mes_nombre} de {año}: {nombre}"
        lista.append({
            "fecha": fecha.isoformat(),
            "nombre": nombre,
            "descripcion": descripcion
        })

    return lista

@app.get("/feriados/{year}", response_class=JSONResponse)
def get_feriados(year: int,
                 mes: Optional[int] = Query(None, ge=1, le=12),
                 desde: Optional[str] = Query(None),
                 hasta: Optional[str] = Query(None)):
    feriados = obtener_feriados_narrativos(year, mes, desde, hasta)
    return {"año": year, "feriados": feriados}
