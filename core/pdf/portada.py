from reportlab.platypus import Paragraph, Spacer, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT


def generar_portada(elementos, mes, anio):

    estilo_empresa = ParagraphStyle("empresa", fontSize=12, alignment=TA_LEFT)
    estilo_titulo = ParagraphStyle("titulo", fontSize=18, alignment=TA_CENTER)
    estilo_ciudad = ParagraphStyle("ciudad", fontSize=16, alignment=TA_CENTER)
    estilo_footer = ParagraphStyle("footer", fontSize=9, alignment=TA_CENTER)

    elementos.append(Paragraph(
        "Dirección de Personal y Recursos Humanos, S.C.P.",
        estilo_empresa
    ))

    elementos.append(Spacer(1,20))

    logo = Image("assets/logo_dprh.png", width=4*cm, height=2*cm)
    logo.hAlign = "RIGHT"
    elementos.append(logo)

    elementos.append(Spacer(1,40))

    elementos.append(Paragraph(
        "Estudio comparativo de sueldos y prestaciones",
        estilo_titulo
    ))

    elementos.append(Spacer(1,40))

    imagen = Image("assets/portada_estudio.png", width=12*cm, height=10*cm)
    imagen.hAlign = "CENTER"
    elementos.append(imagen)

    elementos.append(Spacer(1,40))

    elementos.append(Paragraph(
        f"Yucatán. {mes} {anio}",
        estilo_ciudad
    ))

    elementos.append(Spacer(1,80))

    footer = Paragraph("""
Dirección de Personal y Recursos Humanos, S.C.P<br/>
Calle 29-A No. 257 x 28 y 30 Col. Alemán, Mérida, Yucatán, México<br/>
Tel. (999) 927.27.54 al 56 - Email: merida@dprh.com.mx<br/>
Sitio web: www.dprh.com.mx
""", estilo_footer)

    elementos.append(footer)