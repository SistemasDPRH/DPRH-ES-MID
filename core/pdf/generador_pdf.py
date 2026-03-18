from reportlab.platypus import SimpleDocTemplate

# SECCIONES
from core.secciones.portada import generar_portada
from core.secciones.indice import pagina_tabla_contenido
from core.secciones.objetivo import pagina_objetivo
from core.secciones.caracteristicas import pagina_caracteristicas_encuesta
from core.secciones.indicadores import pagina_indicadores
from core.secciones.informacion_general import pagina_informacion_general
from core.secciones.tabulador_sueldos import pagina_tabulador_sueldos

# LECTORES
from core.lector_dprh import leer_carpeta_dprh
from core.lector_excel import leer_tabulador_excel


def generar_pdf(
    ruta_pdf,
    carpeta_dprh,
    ruta_excel,
    mes,
    anio
):

    pdf = SimpleDocTemplate(
        ruta_pdf,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=30
    )
    elementos = []

    # =========================
    # 1. LEER DATOS
    # =========================
    datos_dprh = leer_carpeta_dprh(carpeta_dprh)
    datos_excel = leer_tabulador_excel(ruta_excel)

    # =========================
    # 2. PORTADA
    # =========================
    generar_portada(elementos, mes, anio)

    # =========================
    # 3. INDICE
    # =========================
    pagina_tabla_contenido(elementos)

    # =========================
    # 4. OBJETIVO
    # =========================
    pagina_objetivo(elementos)

    # =========================
    # 5. CARACTERISTICAS
    # =========================
    pagina_caracteristicas_encuesta(elementos, datos_dprh)

    # =========================
    # 6. INDICADORES ECONOMICOS
    # =========================
    pagina_indicadores(elementos)

    # =========================
    # 7. INFORMACION GENERAL
    # =========================
    pagina_informacion_general(elementos, datos_dprh)

    # =========================
    # 8. TABULADOR
    # =========================
    pagina_tabulador_sueldos(elementos, datos_excel)

    # =========================
    # BUILD
    # =========================
    pdf.build(elementos)