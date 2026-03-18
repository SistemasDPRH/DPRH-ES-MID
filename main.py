from core.pdf.generador_pdf import generar_pdf


if __name__ == "__main__":

    generar_pdf(
        ruta_pdf="estudios_generados/estudio_final.pdf",
        carpeta_dprh="estudios/",          # carpeta con .dprh
        ruta_excel="tabulador.xlsx",       # tu Excel
        mes="Abril",
        anio="2025"
    )