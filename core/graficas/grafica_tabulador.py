import matplotlib.pyplot as plt

def grafica_contrato_colectivo(empresas, ruta_salida):

    total = len(empresas)

    si = sum(1 for e in empresas if e.get("ContratoColectivoSi"))
    no = sum(1 for e in empresas if e.get("ContratoColectivoNo"))

    valores = [si, no]
    etiquetas = ["Sí", "No"]

    plt.figure()

    plt.pie(
        valores,
        labels=etiquetas,
        autopct="%1.1f%%"
    )

    plt.title("Contrato Colectivo")

    plt.savefig(ruta_salida)
    plt.close()