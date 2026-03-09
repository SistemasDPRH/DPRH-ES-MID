from lector_dprh import leer_archivos_dprh
from generador_pdf import generar_pdf

carpeta_datos = "datos_empresas"

datos = leer_archivos_dprh(carpeta_datos)

generar_pdf(
    "estudio_sueldos_2026.pdf",
    "Abril",
    "2026",
    datos
)