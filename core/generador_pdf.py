from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY


# ===============================
# PORTADA
# ===============================

def generar_portada(elementos, mes, anio):

    estilo_empresa = ParagraphStyle(
        name="empresa",
        fontSize=12,
        alignment=TA_LEFT
    )

    estilo_titulo = ParagraphStyle(
        name="titulo",
        fontSize=18,
        alignment=TA_CENTER
    )

    estilo_ciudad = ParagraphStyle(
        name="ciudad",
        fontSize=16,
        alignment=TA_CENTER
    )

    estilo_footer = ParagraphStyle(
        name="footer",
        fontSize=9,
        alignment=TA_CENTER
    )

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


# ===============================
# TABLA DE CONTENIDO
# ===============================

def pagina_tabla_contenido(elementos):

    titulo = ParagraphStyle(
        name="titulo_indice",
        fontSize=18,
        alignment=TA_CENTER
    )

    texto = ParagraphStyle(
        name="texto_indice",
        fontSize=11,
        alignment=TA_LEFT
    )

    elementos.append(PageBreak())

    elementos.append(Paragraph("TABLA DE CONTENIDO", titulo))
    elementos.append(Spacer(1,30))

    contenido = [

"I.- Nuestra Responsabilidad",
"   - Alcance de nuestra responsabilidad.",

"II.- Objetivo",
"   - Objetivo de la realización del estudio.",

"III.- Características de la Encuesta",
"   - Número de puestos y empresas participantes.",
"   - Clasificación por sector empresarial.",

"IV.- Información General",
"   - Indicadores Económicos.",
"   - Vigencia de los datos recabados.",
"   - Tamaño de la muestra encuestada.",
"   - Clasificación de empresas por número de empleados.",
"   - Índice de Rotación del personal.",

"V.- Tabulador de Sueldos y Contrato Colectivo de Trabajo",
"   - Último aumento a sueldos.",
"   - Sueldos de contratación.",
"   - Sindicatos en la empresas.",
"   - Información general de los Contratos Colectivos de Trabajo.",

"VI.- Prestaciones y Beneficios",
"   - Días Adicionales a la Ley y Jornada Semanal.",
"   - Días de Vacaciones, Prima Vacacional y Aguinaldo.",
"   - Seguro de Vida.- Gastos Médico Mayores.",
"   - Fondo de Ahorro.- Asignación de Automóvil.",
"   - Bonos por cumplimiento de metas.- Reparto de Utilidades.",
"   - Incentivos por Puntualidad y Asistencia.",
"   - Comedor, Transporte y Vales de Despensa.",
"   - Compensación o Bono de Antigüedad.",
"   - Previsión Social.",
"   - Prestaciones Adicionales.",

"VII.- Salarios Mínimos",
"   - Distribución de Puestos y número de Empleados de acuerdo al rango de Salarios Mínimos.",
"   - Tabla de Puestos por Salarios Minimos.",

"VIII.- Evaluación Comparativa de Sueldos",
"   - Descripción genérica del puesto.",
"   - Estadística descriptiva sobre cada puesto.",

"IX.- Apéndice - Glosario y Conceptos Estadísticos",
"   - Tablas de Información General.",
"   - Tablas de Tabulador de Sueldos y Contrato Colectivo de Trabajo.",
"   - Tablas de Prestaciones.",
"   - Estadística descriptiva de Sueldos y detalle por Empresa.",
"   - Estadística descriptiva de Sueldos clasificado de acuerdo a sus Niveles de ventas anuales.",
"   - Desarrollo de la estructura de puestos."
]

    for linea in contenido:

        elementos.append(Paragraph(linea, texto))
        elementos.append(Spacer(1,5))


# ===============================
# NUESTRA RESPONSABILIDAD
# ===============================

def pagina_responsabilidad(elementos):

    estilo_titulo = ParagraphStyle(
        name="titulo_seccion",
        fontSize=16,
        alignment=TA_CENTER
    )

    estilo_subtitulo = ParagraphStyle(
        name="subtitulo",
        fontSize=13,
        alignment=TA_CENTER
    )

    estilo_texto = ParagraphStyle(
        name="texto",
        fontSize=10,
        alignment=TA_JUSTIFY,
        leading=14
    )

    elementos.append(PageBreak())

    elementos.append(Paragraph(
        "I.- Nuestra Responsabilidad",
        estilo_titulo
    ))

    elementos.append(Spacer(1,20))

    elementos.append(Paragraph(
        "Alcance de nuestra responsabilidad",
        estilo_subtitulo
    ))

    elementos.append(Spacer(1,30))

    texto_responsabilidad = [

"""El presente Estudio de Sueldos y Prestaciones, realizado por Dirección de Personal y Recursos Humanos SCP (DPRH) y los resultados de los mismos, incluyendo aquellos informes relacionados se realizan y están disponibles para la Empresa Solicitante de conformidad con los siguientes términos y condiciones:""",

"<b>Términos y Condiciones.</b>",

"""Calidad de Servicio. DPRH requerirá de la(s) persona(a) física o moral solicitante(s), los datos que crea necesarios para llevar a cabo dicho Estudio. DPRH proporcionará los formatos de captura de la manera que considere conveniente para permitir su proceso. El Solicitante tendrá la responsabilidad de verificar que cada entrega de datos sea veraz, precisa y completa, un asociado de DPRH revisará cada entrega de datos para verificar su razonabilidad y podrá cuestionar aquellos que considere necesarios. Cuando el Estudio involucre a un grupo de Empresas participantes, DPRH se reserva la fecha de entrega de los resultados y dependerá del cumplimiento de los plazos de entrega de datos por parte de los participantes.""",

"""Derechos de Propiedad Intelectual. DPRH retendrá la titularidad y el derecho de propiedad intelectual sobre estos Estudios. El uso no-autorizado o la duplicación de los mismos, sin el previo consentimiento de DPRH, quedan expresamente prohibidos.""",

"""El uso de la información incluida en los Estudios no sustituye la obtención de asesoramiento legal, consultoría o cualquier otro tipo de asesoramiento necesario para determinar si las prácticas y los niveles de compensación son razonables o adecuados.""",

"""Uso del Estudio. Usted tendrá el derecho de utilizar el resultado del Estudio únicamente dentro de su empresa para propósitos de planificación interna de compensación y no podrán ser modificados, reproducidos, vendidos o transferidos en su totalidad o parcialmente. Si Usted quisiese compartir las encuestas (en todo o en parte) con un tercero deberá obtener el previo consentimiento de DPRH.""",

"""Limitación de Responsabilidad. La responsabilidad conjunta de DPRH y sus empleados, directores, ejecutivos y agentes ante el Solicitante por cualquier pérdida relacionada con la prestación de nuestros servicios no excederá el precio facturado por la realización del Estudio o el monto total de los honorarios pagados a DPRH durante un periodo de doce meses contados a partir del inicio del servicio.""",

"""General. La validez e interpretación de estos términos se regirán por las leyes del Estado de Yucatán, México. Las partes se someten a la jurisdicción exclusiva de las cortes del Estado de Yucatán para resolver cualquier controversia relacionada con estos estudios.""",

"<b>Confidencialidad</b>",

"""Confidencialidad y Uso de los Datos. Los datos de los participantes suministrados a las encuestas serán confidenciales. DPRH toma las precauciones y medidas de seguridad razonables para prevenir el acceso no autorizado por terceros.""",

"""Esta información es exclusivamente para el uso interno de los clientes de DPRH y con el único propósito de participar en las encuestas de DPRH. Ninguna persona podrá utilizar o reproducir esta información para ningún otro propósito."""
]

    for parrafo in texto_responsabilidad:

        elementos.append(Paragraph(parrafo, estilo_texto))
        elementos.append(Spacer(1,12))


# ===============================
# GENERADOR FINAL
# ===============================

def generar_pdf(ruta_pdf, mes, anio):

    pdf = SimpleDocTemplate(ruta_pdf, pagesize=letter)

    elementos = []

    generar_portada(elementos, mes, anio)

    pagina_tabla_contenido(elementos)

    pagina_responsabilidad(elementos)

    pdf.build(elementos)