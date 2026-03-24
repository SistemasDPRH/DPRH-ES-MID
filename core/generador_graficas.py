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

def safe_int(valor):
    try:
        if valor is None or valor == "":
            return 0
        return int(str(valor).replace(",", "").strip())
    except:
        return 0


def grafica_sindical(empresas_data):

    total_no_sind = 0
    total_sind = 0

    for data in empresas_data:

        no_sind = safe_int(data.get("NumeroEmpleadosNoSind"))
        sind = safe_int(data.get("NumeroEmpleadosSind"))

        total_no_sind += no_sind
        total_sind += sind

    print(f"DEBUG -> No Sind: {total_no_sind}, Sind: {total_sind}")

    # 🔴 PROTECCIÓN TOTAL
    if total_no_sind == 0 and total_sind == 0:
        print("⚠️ No hay datos para gráfica sindical")
        return

    # evitar valores negativos o raros
    valores = [
        max(total_no_sind, 0),
        max(total_sind, 0)
    ]

    total = sum(valores)

    if total == 0:
        print("⚠️ Datos inválidos para gráfica")
        return

    plt.figure()

    plt.pie(
        valores,
        labels=["No Sindicalizados", "Sindicalizados"],
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Distribución Sindical")

    plt.savefig("assets/grafica_sindical.png")
    plt.close()