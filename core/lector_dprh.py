import os

def parsear_dprh(ruta_archivo):

    datos = {}

    with open(ruta_archivo, "r", encoding="utf-8") as f:

        for linea in f:

            linea = linea.strip()

            if "|" in linea:

                clave, valor = linea.split("|", 1)

                datos[clave] = valor

    return datos


def leer_carpeta_dprh(carpeta):

    empresas = []
    sectores = {}
    total_empleados = 0

    for archivo in os.listdir(carpeta):

        if archivo.endswith(".dprh"):

            ruta = os.path.join(carpeta, archivo)

            data = parsear_dprh(ruta)

            empresas.append(data["RazonComercial"])

            sector = data.get("SectorEmpresarial","Desconocido")

            sectores[sector] = sectores.get(sector,0) + 1

            # empleados
            no_sind = data.get("NumeroEmpleadosNoSind","0").replace(",","")
            sind = data.get("NumeroEmpleadosSind","0").replace(",","")

            total_empleados += int(no_sind) + int(sind)

    return {
        "numero_empresas": len(empresas),
        "lista_empresas": empresas,
        "sectores": sectores,
        "total_empleados": total_empleados
    }