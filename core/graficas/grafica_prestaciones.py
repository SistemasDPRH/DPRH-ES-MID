import matplotlib.pyplot as plt

def grafica_si_no(empresas, campo_si, campo_no, titulo, ruta):

    si = sum(1 for e in empresas if e.get(campo_si))
    no = sum(1 for e in empresas if e.get(campo_no))

    plt.figure()
    plt.pie([si, no], labels=["Sí","No"], autopct="%1.1f%%")
    plt.title(titulo)
    plt.savefig(ruta)
    plt.close()