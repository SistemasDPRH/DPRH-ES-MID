import os
from core.lector_dprh import leer_dprh
from core.lector_excel import leer_excel


def cargar_empresas(carpeta):

    empresas = []

    for empresa in os.listdir(carpeta):

        ruta_empresa = os.path.join(carpeta, empresa)

        if not os.path.isdir(ruta_empresa):
            continue

        archivo_dprh = None
        archivo_excel = None

        for archivo in os.listdir(ruta_empresa):

            if archivo.endswith(".dprh"):
                archivo_dprh = os.path.join(ruta_empresa, archivo)

            if archivo.endswith(".xlsx") or archivo.endswith(".xlsm"):
                archivo_excel = os.path.join(ruta_empresa, archivo)

        if archivo_dprh and archivo_excel:

            datos_empresa = {
                "nombre": empresa,
                "info": leer_dprh(archivo_dprh),
                "sueldos": leer_excel(archivo_excel)
            }

            empresas.append(datos_empresa)

    return empresas