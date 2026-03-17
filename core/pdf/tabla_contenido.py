from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT


def pagina_tabla_contenido(elementos):

    titulo = ParagraphStyle("titulo", fontSize=18, alignment=TA_CENTER)
    texto = ParagraphStyle("texto", fontSize=11, alignment=TA_LEFT)

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