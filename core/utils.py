import os


def validar_estructura(carpeta):

    errores = []

    for empresa in os.listdir(carpeta):

        ruta_empresa = os.path.join(carpeta, empresa)

        if os.path.isdir(ruta_empresa):

            tiene_dprh = False
            tiene_excel = False

            for archivo in os.listdir(ruta_empresa):

                if archivo.endswith(".dprh"):
                    tiene_dprh = True

                if archivo.endswith(".xlsx"):
                    tiene_excel = True

            if not tiene_dprh or not tiene_excel:
                errores.append(empresa)

    return errores

def validar_y_filtrar_empresas(carpeta):

    empresas_validas = []
    empresas_invalidas = []

    for empresa in os.listdir(carpeta):

        ruta_empresa = os.path.join(carpeta, empresa)

        if os.path.isdir(ruta_empresa):

            tiene_dprh = False
            tiene_excel = False

            for archivo in os.listdir(ruta_empresa):

                if archivo.endswith(".dprh"):
                    tiene_dprh = True

                if archivo.endswith((".xlsx", ".xlsm")):
                    tiene_excel = True

            if tiene_dprh and tiene_excel:
                empresas_validas.append(empresa)
            else:
                empresas_invalidas.append(empresa)

    return empresas_validas, empresas_invalidas