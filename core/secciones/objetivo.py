from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER


def pagina_objetivo(elementos):

    titulo = ParagraphStyle("titulo", fontSize=18, alignment=TA_CENTER)
    texto = ParagraphStyle("texto", fontSize=12, alignment=TA_CENTER, leading=20)

    elementos.append(PageBreak())

    elementos.append(Spacer(1,200))

    elementos.append(Paragraph("OBJETIVO", titulo))
    elementos.append(Spacer(1,40))

    contenido = """
Proporcionar información completa y oportuna sobre la situación actual de sueldos y prestaciones en el estado de Yucatán a las empresas participantes, permitiendo tomar decisiones adecuadas y competitivas dentro del mercado laboral.
"""

    elementos.append(Paragraph(contenido, texto))