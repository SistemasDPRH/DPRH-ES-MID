from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY


def pagina_responsabilidad(elementos):

    estilo_titulo = ParagraphStyle(
        "titulo",
        fontSize=16,
        alignment=TA_CENTER
    )

    estilo_texto = ParagraphStyle(
        "texto",
        fontSize=10,
        alignment=TA_JUSTIFY,
        leading=14
    )

    elementos.append(PageBreak())

    # TÍTULO
    elementos.append(Paragraph("NUESTRA RESPONSABILIDAD", estilo_titulo))
    elementos.append(Spacer(1,20))

    # TEXTO EXACTO DEL PDF
    texto = """
El  presente  Estudio  de  Sueldos  y  Prestaciones,  realizado  por  Dirección  de  Personal  y  Recursos  Humanos  SCP, 
(DPRH)  y  los  resultados  de  los  mismos,  incluyendo  aquellos  informes  relacionados  se  realizan  y  están  disponibles 
para la Empresa Solicitante de conformidad con los siguientes términos y condiciones:

DPRH proporcionará los formatos de captura de los datos que crea necesarios para llevar a cabo dicho Estudio.

La(s) persona(s) física o moral solicitante(s), relacionada(s) a la información (“Personas Relacionadas”), será responsable de proporcionar información veraz y oportuna.

DPRH no asume responsabilidad alguna frente a terceros por el uso indebido de la información contenida en el presente estudio.

DPRH retendrá la titularidad y el derecho de propiedad intelectual del presente estudio.
"""

    elementos.append(Paragraph(texto, estilo_texto))