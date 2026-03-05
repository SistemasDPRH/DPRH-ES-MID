# core/lector_dprh.py

def leer_dprh(ruta):
    datos = {}

    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            if "|" in linea:
                clave, valor = linea.strip().split("|", 1)
                datos[clave] = valor

    return datos