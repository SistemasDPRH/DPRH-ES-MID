from reportlab.platypus import SimpleDocTemplate

# SECCIONES
from core.secciones.portada import generar_portada
from core.secciones.indice import pagina_tabla_contenido
from core.secciones.objetivo import pagina_objetivo
from core.secciones.caracteristicas import pagina_caracteristicas_encuesta
from core.secciones.indicadores import pagina_indicadores
from core.secciones.info_general import pagina_informacion_general
from core.secciones.tabulador_sueldos import pagina_tabulador_sueldos

# GRÁFICAS
from core.generador_graficas import grafica_sectores, grafica_sindical

# LECTORES
from core.lector_dprh import leer_carpeta_dprh
from core.lector_excel import leer_todos_los_tabuladores

# PROCESADOR
from core.procesador_tabulador import procesar_tabulador_completo


def generar_pdf(
    ruta_pdf,
    carpeta_dprh,
    mes,
    anio
):

    pdf = SimpleDocTemplate(
        ruta_pdf,
        rightMargin=35,
        leftMargin=35,
        topMargin=40,
        bottomMargin=30
    )

    elementos = []

    # =========================
    # 1. LEER DATOS DPRH
    # =========================
    datos_dprh = leer_carpeta_dprh(carpeta_dprh)

    # 🔹 Mostrar empresas incompletas
    if datos_dprh["empresas_incompletas"]:
        print("⚠️ Empresas con archivos incompletos:")
        for e in datos_dprh["empresas_incompletas"]:
            print(f"- {e}")

    # =========================
    # 2. GRÁFICAS
    # =========================
    grafica_sectores(datos_dprh["sectores"])
    grafica_sindical(datos_dprh["empresas_data"])

    # =========================
    # 3. LEER EXCEL (TODAS LAS EMPRESAS)
    # =========================
    datos_excel = leer_todos_los_tabuladores(datos_dprh["empresas_data"])

    # =========================
    # 4. PROCESAR TABULADOR (🔥 CLAVE)
    # =========================
    tabulador = procesar_tabulador_completo(datos_excel)

    # =========================
    # 5. PORTADA
    # =========================
    generar_portada(elementos, mes, anio)

    # =========================
    # 6. ÍNDICE
    # =========================
    pagina_tabla_contenido(elementos)

    # =========================
    # 7. OBJETIVO
    # =========================
    pagina_objetivo(elementos)

    # =========================
    # 8. CARACTERÍSTICAS
    # =========================
    pagina_caracteristicas_encuesta(elementos, datos_dprh)

    # =========================
    # 9. INDICADORES ECONÓMICOS
    # =========================
    pagina_indicadores(elementos)

    # =========================
    # 10. INFORMACIÓN GENERAL
    # =========================
    pagina_informacion_general(elementos, datos_dprh)

    # =========================
    # 11. TABULADOR FINAL 🔥
    # =========================
    pagina_tabulador_sueldos(elementos, tabulador)

    # =========================
    # BUILD PDF
    # =========================
    print("📄 Generando PDF final...")
    pdf.build(elementos)

    print("✅ PDF generado correctamente")