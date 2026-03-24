import numpy as np
from collections import defaultdict


def calcular_estadisticas(valores, pesos=None):

    arr = np.array(valores)

    if len(arr) == 0:
        return None

    stats = {
        "min": float(np.min(arr)),
        "q1": float(np.percentile(arr, 25)),
        "mediana": float(np.percentile(arr, 50)),
        "q3": float(np.percentile(arr, 75)),
        "max": float(np.max(arr)),
        "media": float(np.mean(arr)),
        "std": float(np.std(arr))
    }

    # 🔥 MEDIA PONDERADA
    if pesos and sum(pesos) > 0:
        stats["media_ponderada"] = float(np.average(arr, weights=pesos))
    else:
        stats["media_ponderada"] = stats["media"]

    return stats


def agrupar_por_puesto(datos_excel):

    agrupado = defaultdict(list)

    for fila in datos_excel:
        puesto = fila["puesto"]
        agrupado[puesto].append(fila)

    return agrupado


def procesar_tabulador_completo(datos_excel):

    agrupado = agrupar_por_puesto(datos_excel)

    resultado_final = []

    for puesto, registros in agrupado.items():

        # -----------------------------
        # SUELDO BASE
        # -----------------------------
        sueldos_base = [r["sueldo_base"] for r in registros if r["sueldo_base"] > 0]
        empleados = [r["empleados"] for r in registros if r["sueldo_base"] > 0]

        stats_base = calcular_estadisticas(sueldos_base, empleados)

        # -----------------------------
        # SUELDO NETO
        # -----------------------------
        sueldos_neto = [r["sueldo_neto"] for r in registros if r["sueldo_neto"] > 0]
        empleados_neto = [r["empleados"] for r in registros if r["sueldo_neto"] > 0]

        stats_neto = calcular_estadisticas(sueldos_neto, empleados_neto)

        # -----------------------------
        # SUELDO INTEGRADO
        # -----------------------------
        sueldos_int = [r["sueldo_integrado"] for r in registros if r["sueldo_integrado"] > 0]
        empleados_int = [r["empleados"] for r in registros if r["sueldo_integrado"] > 0]

        stats_int = calcular_estadisticas(sueldos_int, empleados_int)

        if not stats_base:
            continue

        resultado_final.append({
            "puesto": puesto,

            "base": stats_base,
            "neto": stats_neto,
            "integrado": stats_int,

            # info adicional (para tabla inferior)
            "detalle": registros
        })

    return resultado_final