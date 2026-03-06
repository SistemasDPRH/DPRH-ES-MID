import pandas as pd


def leer_excel(ruta):

    df = pd.read_excel(
        ruta,
        sheet_name=0,
        header=0
    )

    df = df.iloc[:540]

    return df