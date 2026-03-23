import os
import pandas as pd


def leer_tabuladores_carpeta(carpeta_principal):

    dataframes = []

    for empresa in os.listdir(carpeta_principal):

        ruta_empresa = os.path.join(carpeta_principal, empresa)

        if os.path.isdir(ruta_empresa):

            for archivo in os.listdir(ruta_empresa):

                if archivo.endswith((".xlsx", ".xlsm")):

                    ruta_excel = os.path.join(ruta_empresa, archivo)

                    try:
                        df = pd.read_excel(ruta_excel, sheet_name=0)

                        df["Empresa"] = empresa

                        dataframes.append(df)

                    except Exception as e:
                        print(f"Error leyendo {ruta_excel}: {e}")

    if dataframes:
        return pd.concat(dataframes, ignore_index=True)

    return pd.DataFrame()