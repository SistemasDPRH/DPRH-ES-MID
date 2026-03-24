import os


def convertir_entero(valor):
    try:
        return int(str(valor).replace(",", "").strip())
    except:
        return 0


def parsear_dprh(ruta_archivo):
    datos = {}

    with open(ruta_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if "|" in linea:
                clave, valor = linea.split("|", 1)
                datos[clave] = valor

    return datos


def leer_carpeta_dprh(carpeta_principal):

    empresas_data = []
    empresas_incompletas = []
    sectores = {}
    total_empleados = 0

    # recorrer carpetas de empresas
    for nombre_empresa in os.listdir(carpeta_principal):

        ruta_empresa = os.path.join(carpeta_principal, nombre_empresa)

        if not os.path.isdir(ruta_empresa):
            continue

        archivo_dprh = None
        archivo_excel = None

        # buscar archivos dentro de la carpeta
        for archivo in os.listdir(ruta_empresa):

            if archivo.endswith(".dprh"):
                archivo_dprh = os.path.join(ruta_empresa, archivo)

            if archivo.endswith(".xlsx") or archivo.endswith(".xlsm"):
                archivo_excel = os.path.join(ruta_empresa, archivo)

        # validar existencia
        if not archivo_dprh or not archivo_excel:
            faltantes = []
            if not archivo_dprh:
                faltantes.append("DPRH")
            if not archivo_excel:
                faltantes.append("Excel")

            empresas_incompletas.append(
                f"{nombre_empresa} → falta {', '.join(faltantes)}"
            )
            continue

        # leer DPRH
        data = parsear_dprh(archivo_dprh)

        # empleados
        no_sind = convertir_entero(data.get("NumeroEmpleadosNoSind", 0))
        sind = convertir_entero(data.get("NumeroEmpleadosSind", 0))

        total_empleados += no_sind + sind

        # sector
        sector = data.get("SectorEmpresarial", "Desconocido")
        sectores[sector] = sectores.get(sector, 0) + 1

        # guardar info completa de empresa
        empresas_data.append({
            "nombre": data.get("RazonComercial", nombre_empresa),
            "sector": sector,
            "no_sind": no_sind,
            "sind": sind,
            "dprh": data,
            "excel_path": archivo_excel
        })

    return {
        "numero_empresas": len(empresas_data),
        "empresas_data": empresas_data,
        "empresas_incompletas": empresas_incompletas,
        "sectores": sectores,
        "total_empleados": total_empleados
    }