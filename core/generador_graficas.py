import matplotlib.pyplot as plt


# =========================
# GRAFICA SECTORES
# =========================
def grafica_sectores(sectores):

    labels = list(sectores.keys())
    valores = list(sectores.values())

    plt.figure()

    plt.pie(
        valores,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Clasificación por Sector Empresarial")

    plt.savefig("assets/grafica_sectores.png")
    plt.close()


# =========================
# GRAFICA SINDICAL
# =========================
def grafica_sindical(datos_empresas):

    total_sind = 0
    total_no_sind = 0

    for emp in datos_empresas:

        try:
            total_sind += int(emp.get("NumeroEmpleadosSind", 0))
            total_no_sind += int(emp.get("NumeroEmpleadosNoSind", 0))
        except:
            pass

    plt.figure()

    plt.pie(
        [total_no_sind, total_sind],
        labels=["No Sindicalizados", "Sindicalizados"],
        autopct="%1.2f%%",
        startangle=90
    )

    plt.title("Distribución Sindical")

    plt.savefig("assets/grafica_sindical.png")
    plt.close()