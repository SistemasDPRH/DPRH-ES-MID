import os


def convertir_valor(valor):
    """
    Convierte valores del .dprh a tipos útiles
    """
    if valor == "True":
        return True
    if valor == "False":
        return False

    # intentar número
    try:
        return float(valor.replace(",", ""))
    except:
        return valor


def parsear_dprh(ruta_archivo):

    datos = {}

    with open(ruta_archivo, "r", encoding="utf-8") as f:

        for linea in f:
            linea = linea.strip()

            if "|" in linea:
                clave, valor = linea.split("|", 1)
                datos[clave] = convertir_valor(valor)

    return datos


def leer_carpeta_dprh(carpeta):

    empresas = []

    for archivo in os.listdir(carpeta):

        if archivo.endswith(".dprh"):

            ruta = os.path.join(carpeta, archivo)
            data = parsear_dprh(ruta)

            empresas.append(data)  # 🔥 AQUÍ ESTÁ EL CAMBIO CLAVE

    return empresas