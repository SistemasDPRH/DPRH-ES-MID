import os


def convertir_valor(valor):

    if valor == "True":
        return True
    if valor == "False":
        return False

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

    empresas_data = []
    sectores = {}
    total_empleados = 0

    for archivo in os.listdir(carpeta):

        if archivo.endswith(".dprh"):

            ruta = os.path.join(carpeta, archivo)
            data = parsear_dprh(ruta)

            empresas_data.append(data)

            # Sector
            sector = data.get("SectorEmpresarial", "Desconocido")
            sectores[sector] = sectores.get(sector, 0) + 1

            # Empleados
            try:
                no_sind = int(data.get("NumeroEmpleadosNoSind", 0) or 0)
                sind = int(data.get("NumeroEmpleadosSind", 0) or 0)
                total_empleados += no_sind + sind
            except:
                pass

    return {
        "empresas_data": empresas_data,
        "numero_empresas": len(empresas_data),
        "sectores": sectores,
        "total_empleados": total_empleados
    }