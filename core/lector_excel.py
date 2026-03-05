# core/lector_excel.py

import pandas as pd

def leer_excel(ruta):

    df = pd.read_excel(ruta)

    return df