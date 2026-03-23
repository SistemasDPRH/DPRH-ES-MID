from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT


def pagina_tabla_contenido(elementos):

    titulo = ParagraphStyle(
        name="titulo",
        fontSize=18,
        alignment=TA_CENTER
    )

    texto = ParagraphStyle(
        name="texto",
        fontSize=11,
        alignment=TA_LEFT,
        leading=14
    )

    elementos.append(PageBreak())

    elementos.append(Paragraph("TABLA DE CONTENIDO", titulo))
    elementos.append(Spacer(1,30))

    contenido = [
        "I.- Nuestra Responsabilidad",
        "II.- Objetivo",
        "III.- Características de la Encuesta",
        "IV.- Información General",
        "V.- Tabulador de Sueldos",
        "VI.- Prestaciones y Beneficios",
        "VII.- Salarios Mínimos",
        "VIII.- Evaluación Comparativa de Sueldos",
        "IX.- Apéndice"
    ]

    for linea in contenido:
        elementos.append(Paragraph(linea, texto))
        elementos.append(Spacer(1,8))