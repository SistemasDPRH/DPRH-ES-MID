from reportlab.platypus import Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.units import cm


def generar_portada(elementos, mes, anio):

    # =========================
    # ESTILOS
    # =========================
    estilo_empresa = ParagraphStyle(
        "empresa",
        fontName="Helvetica",
        fontSize=11,
        alignment=TA_LEFT
    )

    estilo_titulo = ParagraphStyle(
        "titulo",
        fontName="Helvetica-Bold",
        fontSize=18,
        alignment=TA_CENTER
    )

    estilo_ciudad = ParagraphStyle(
        "ciudad",
        fontName="Helvetica",
        fontSize=14,
        alignment=TA_CENTER
    )

    estilo_footer = ParagraphStyle(
        "footer",
        fontName="Helvetica",
        fontSize=9,
        alignment=TA_CENTER,
        leading=12
    )

    # =========================
    # HEADER (EMPRESA + LOGO)
    # =========================
    empresa = Paragraph(
        "Dirección de Personal y Recursos Humanos, S.C.P.",
        estilo_empresa
    )

    logo = Image("assets/logo_dprh.png", width=4*cm, height=2*cm)

    tabla_header = Table(
        [[empresa, logo]],
        colWidths=[12*cm, 4*cm]
    )

    tabla_header.setStyle(TableStyle([
        ("ALIGN", (1,0), (1,0), "RIGHT"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))

    elementos.append(tabla_header)

    elementos.append(Spacer(1, 50))

    # =========================
    # TITULO
    # =========================
    titulo = Paragraph(
        "Estudio comparativo de sueldos y prestaciones",
        estilo_titulo
    )

    elementos.append(titulo)

    elementos.append(Spacer(1, 50))

    # =========================
    # IMAGEN CENTRAL
    # =========================
    imagen = Image(
        "assets/portada_estudio.png",
        width=13*cm,
        height=10*cm
    )
    imagen.hAlign = "CENTER"

    elementos.append(imagen)

    elementos.append(Spacer(1, 40))

    # =========================
    # UBICACION
    # =========================
    ciudad = Paragraph(
        f"Yucatán. {mes} {anio}",
        estilo_ciudad
    )

    elementos.append(ciudad)

    elementos.append(Spacer(1, 70))

    # =========================
    # FOOTER
    # =========================
    footer_texto = """
Dirección de Personal y Recursos Humanos, S.C.P<br/>
Calle 29-A No. 257 x 28 y 30 Col. Alemán, Mérida, Yucatán, México<br/>
Tel. (999) 927.27.54 al 56 - Email: merida@dprh.com.mx<br/>
Sitio web: www.dprh.com.mx
"""

    footer = Paragraph(footer_texto, estilo_footer)

    elementos.append(footer)