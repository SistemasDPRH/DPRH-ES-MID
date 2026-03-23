from reportlab.platypus import Paragraph, Spacer, PageBreak, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.units import cm


def pagina_informacion_general(elementos, datos):

    estilo_titulo = ParagraphStyle(
        name="titulo",
        fontName="Helvetica-Bold",
        fontSize=14,
        alignment=TA_CENTER
    )

    estilo_texto = ParagraphStyle(
        name="texto",
        fontName="Helvetica",
        fontSize=11,
        alignment=TA_JUSTIFY,
        leading=14
    )

    elementos.append(PageBreak())

    # TÍTULO
    elementos.append(Paragraph(
        "IV.- Información General",
        estilo_titulo
    ))

    elementos.append(Spacer(1,20))

    # TEXTO DINÁMICO
    texto = f"""
En el presente estudio participaron {datos.get("numero_empresas",0)} empresas, 
con un total de {datos.get("total_empleados",0)} empleados.
"""

    elementos.append(Paragraph(texto, estilo_texto))

    elementos.append(Spacer(1,30))

    # GRAFICA (SI EXISTE)
    try:
        img = Image("assets/grafica_sindical.png", width=16*cm, height=9*cm)
        img.hAlign = "CENTER"
        elementos.append(img)
    except:
        pass