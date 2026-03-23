import matplotlib.pyplot as plt


def grafica_sectores(sectores, ruta_salida):

    etiquetas = list(sectores.keys())
    valores = list(sectores.values())

    plt.figure()

    plt.pie(
        valores,
        labels=etiquetas,
        autopct="%1.0f%%"
    )

    plt.title("Sectores de empresas participantes")

    plt.savefig(ruta_salida)

    plt.close()