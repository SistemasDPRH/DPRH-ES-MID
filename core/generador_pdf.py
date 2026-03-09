
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors


# =====================================================
# PORTADA
# =====================================================

def generar_portada(elementos, mes, anio):

    estilo_empresa = ParagraphStyle("empresa", fontSize=12, alignment=TA_LEFT)
    estilo_titulo = ParagraphStyle("titulo", fontSize=18, alignment=TA_CENTER)
    estilo_ciudad = ParagraphStyle("ciudad", fontSize=16, alignment=TA_CENTER)
    estilo_footer = ParagraphStyle("footer", fontSize=9, alignment=TA_CENTER)

    empresa = Paragraph(
        "Dirección de Personal y Recursos Humanos, S.C.P.",
        estilo_empresa
    )

    elementos.append(empresa)
    elementos.append(Spacer(1,20))

    logo = Image("assets/logo_dprh.png", width=4*cm, height=2*cm)
    logo.hAlign = "RIGHT"
    elementos.append(logo)

    elementos.append(Spacer(1,40))

    titulo = Paragraph(
        "Estudio comparativo de sueldos y prestaciones",
        estilo_titulo
    )
    elementos.append(titulo)

    elementos.append(Spacer(1,40))

    imagen = Image(
        "assets/portada_estudio.png",
        width=12*cm,
        height=10*cm
    )
    imagen.hAlign = "CENTER"
    elementos.append(imagen)

    elementos.append(Spacer(1,40))

    ciudad = Paragraph(
        f"Yucatán. {mes} {anio}",
        estilo_ciudad
    )
    elementos.append(ciudad)

    elementos.append(Spacer(1,80))

    footer_texto = """
Dirección de Personal y Recursos Humanos, S.C.P<br/>
Calle 29-A No. 257 x 28 y 30 Col. Alemán, Mérida, Yucatán, México<br/>
Tel. (999) 927.27.54 al 56 - Email: merida@dprh.com.mx<br/>
Sitio web: www.dprh.com.mx
"""

    footer = Paragraph(footer_texto, estilo_footer)
    elementos.append(footer)


# =====================================================
# TABLA DE CONTENIDO
# =====================================================

def pagina_tabla_contenido(elementos):

    titulo = ParagraphStyle("titulo_indice", fontSize=18, alignment=TA_CENTER)
    texto = ParagraphStyle("texto_indice", fontSize=11, alignment=TA_LEFT)

    elementos.append(PageBreak())

    elementos.append(Paragraph("TABLA DE CONTENIDO", titulo))
    elementos.append(Spacer(1,30))

    contenido = [
        "I.- Nuestra Responsabilidad",
        "   - Alcance de nuestra responsabilidad.",
        "",
        "II.- Objetivo",
        "   - Objetivo de la realización del estudio.",
        "",
        "III.- Características de la Encuesta",
        "   - Número de puestos y empresas participantes.",
        "   - Clasificación por sector empresarial."
    ]

    for linea in contenido:
        elementos.append(Paragraph(linea, texto))
        elementos.append(Spacer(1,6))


# =====================================================
# OBJETIVO
# =====================================================

def pagina_objetivo(elementos):

    estilo_titulo = ParagraphStyle(
        "titulo_objetivo",
        fontSize=18,
        alignment=TA_CENTER
    )

    estilo_texto = ParagraphStyle(
        "texto_objetivo",
        fontSize=12,
        alignment=TA_CENTER,
        leading=20
    )

    elementos.append(PageBreak())

    elementos.append(Spacer(1,200))

    elementos.append(Paragraph("OBJETIVO", estilo_titulo))

    elementos.append(Spacer(1,40))

    texto = """
Proporcionar información completa y oportuna sobre la situación actual de sueldos y prestaciones en el estado de Yucatán a las empresas participantes, permitiendo tomar decisiones adecuadas y competitivas dentro del mercado laboral.
"""

    elementos.append(Paragraph(texto, estilo_texto))


# =====================================================
# CARACTERÍSTICAS DE LA ENCUESTA
# =====================================================

def pagina_caracteristicas_encuesta(elementos):

    estilo_titulo = ParagraphStyle(
        "titulo",
        fontSize=16,
        alignment=TA_CENTER
    )

    estilo_texto = ParagraphStyle(
        "texto",
        fontSize=11,
        alignment=TA_JUSTIFY
    )

    elementos.append(PageBreak())

    elementos.append(Paragraph(
        "CARACTERÍSTICAS DE LA ENCUESTA",
        estilo_titulo
    ))

    elementos.append(Spacer(1,20))

    texto = f"""
    En el presente estudio participaron {datos["empresas"]} empresas ubicadas en el estado de Yucatán.

    El número de puestos reportados simultáneamente por al menos dos empresas fue de {datos["puestos"]};
    con un total de {datos["empleados"]} empleados asociados a esos puestos.
    """
    elementos.append(Paragraph(texto, estilo_texto))

    elementos.append(Spacer(1,30))

    empresas = [
        ["AEI","Baldesigns de México"],
        ["Bohn de México","Dimadera"],
        ["Dunosusa","Elemetic"],
        ["Empaques Nova","Grupo Crio"],
        ["Industria Salinera de Yucatán","Kekén"],
        ["La Anita","La Lupita"],
        ["Marbol","Millet Industria de Vidrio"],
        ["Milsco de México","Momente Brands"],
        ["Provi","Stuller México"],
        ["The Palace Company","Uchiyama Manufacturing"]
    ]

    tabla = Table(empresas, colWidths=[8*cm,8*cm])

    tabla.setStyle(TableStyle([
        ("FONTNAME",(0,0),(-1,-1),"Helvetica"),
        ("FONTSIZE",(0,0),(-1,-1),10),
        ("BOTTOMPADDING",(0,0),(-1,-1),6)
    ]))

    elementos.append(tabla)

    elementos.append(Spacer(1,30))

    try:
        grafica = Image("assets/grafica_sectores.png", width=16*cm, height=9*cm)
        grafica.hAlign = "CENTER"
        elementos.append(grafica)
    except:
        pass


# =====================================================
# GENERADOR PRINCIPAL
# =====================================================

def generar_pdf(nombre_archivo, mes, anio, datos):

    pdf = SimpleDocTemplate(
        nombre_archivo,
        pagesize=letter
    )

    elementos = []

    generar_portada(elementos, mes, anio)
    pagina_tabla_contenido(elementos)
    pagina_objetivo(elementos)
    pagina_caracteristicas_encuesta(elementos)

    pdf.build(elementos)
