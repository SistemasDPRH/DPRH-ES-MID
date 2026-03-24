import pandas as pd


def limpiar_numero(valor):
    try:
        return float(str(valor).replace(",", "").strip())
    except:
        return 0.0


def leer_tabulador_excel(ruta_excel):

    try:
        df = pd.read_excel(ruta_excel, sheet_name=0)
    except Exception as e:
        print(f"⚠️ Error leyendo Excel: {ruta_excel}")
        return []

    # Normalizar nombres de columnas
    df.columns = [str(col).strip() for col in df.columns]

    datos = []

    for _, row in df.iterrows():

        try:
            registro = {
                "clave": str(row.get("Clave", "")).strip(),
                "area": str(row.get("Área", "")).strip(),
                "puesto": str(row.get("Puesto Homologado", "")).strip(),

                "sueldo_base": limpiar_numero(row.get("Sueldo Base de Contratación", 0)),
                "sueldo_neto": limpiar_numero(row.get("Sueldo Neto", 0)),
                "sueldo_integrado": limpiar_numero(row.get("Sueldo Base Integrado", 0)),

                "empleados": limpiar_numero(row.get("Número de Empleados en el Puesto", 0)),

                "escolaridad": str(row.get("Escolaridad", "")).strip(),
                "experiencia": str(row.get("Experiencia", "")).strip(),
                "idioma": str(row.get("Segundo Idioma", "")).strip(),
                "tipo_puesto": str(row.get("Tipo de Puesto", "")).strip(),
            }

            # evitar filas vacías
            if registro["puesto"]:
                datos.append(registro)

        except Exception as e:
            continue

    return datos

def leer_todos_los_tabuladores(empresas_data):

    todos_los_datos = []

    for empresa in empresas_data:

        ruta_excel = empresa["excel_path"]
        nombre_empresa = empresa["nombre"]

        datos_excel = leer_tabulador_excel(ruta_excel)

        for fila in datos_excel:
            fila["empresa"] = nombre_empresa
            todos_los_datos.append(fila)

    return todos_los_datos