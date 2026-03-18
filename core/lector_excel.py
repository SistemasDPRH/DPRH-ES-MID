import pandas as pd


def leer_tabulador_excel(ruta_excel):

    df = pd.read_excel(ruta_excel, sheet_name=0)

    datos = []

    for _, row in df.iterrows():

        fila = [
            str(row.get("Clave", "")),
            str(row.get("Área", "")),
            str(row.get("Puesto Homologado", "")),
            str(row.get("Sueldo Base de Contratación", "")),
            str(row.get("Sueldo Neto", "")),
            str(row.get("Sueldo Base Integrado", "")),
            str(row.get("Número de Empleados en el Puesto", "")),
            str(row.get("Escolaridad", "")),
            str(row.get("Experiencia", "")),
            str(row.get("Segundo Idioma", "")),
            str(row.get("Tipo de Puesto", "")),
        ]

        datos.append(fila)

    return datos