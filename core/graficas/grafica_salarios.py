import matplotlib.pyplot as plt

def grafica_salarios(distribucion, ruta):

    etiquetas = list(distribucion.keys())
    valores = list(distribucion.values())

    plt.figure()
    plt.bar(etiquetas, valores)

    plt.title("Distribución por Salarios Mínimos")

    plt.savefig(ruta)
    plt.close()