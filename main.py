import os
from tkinter import Tk, filedialog
from core.generador_pdf import generar_pdf
from core.utils import validar_y_filtrar_empresas


def seleccionar_carpeta():

    root = Tk()
    root.withdraw()

    carpeta = filedialog.askdirectory(
        title="Selecciona la carpeta del estudio (Ej: Merida2026)"
    )

    return carpeta


if __name__ == "__main__":

    carpeta = seleccionar_carpeta()

    if not carpeta:
        print("No seleccionaste carpeta")
        exit()

    # =========================
    # VALIDAR Y FILTRAR
    # =========================
    validas, invalidas = validar_y_filtrar_empresas(carpeta)

    if invalidas:
        print("⚠️ Empresas ignoradas (archivos incompletos):")
        for e in invalidas:
            print(f"- {e}")

    if not validas:
        print("❌ No hay empresas válidas para procesar")
        exit()

    # =========================
    # NOMBRE Y AÑO
    # =========================
    nombre = os.path.basename(carpeta)
    anio = "".join(filter(str.isdigit, nombre)) or "2026"
    mes = "Abril"

    # =========================
    # OUTPUT
    # =========================
    carpeta_salida = "estudios_generados"
    os.makedirs(carpeta_salida, exist_ok=True)

    ruta_pdf = os.path.join(carpeta_salida, f"{nombre}.pdf")

    print("Generando PDF...")

    generar_pdf(
        ruta_pdf=ruta_pdf,
        carpeta_dprh=carpeta,
        mes=mes,
        anio=anio
    )

    print(f"✅ PDF generado en: {ruta_pdf}")