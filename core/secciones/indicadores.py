from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.lib.units import cm


def pagina_indicadores(elementos):

    estilo_header = ParagraphStyle(
        "header", fontSize=12, alignment=TA_CENTER, textColor=colors.white
    )

    estilo_texto = ParagraphStyle(
        "texto", fontSize=10, alignment=TA_JUSTIFY, leading=14
    )

    estilo_sub = ParagraphStyle(
        "sub", fontSize=10, alignment=TA_JUSTIFY
    )

    elementos.append(PageBreak())

    # ================= HEADER
    header = Table(
        [[Paragraph("INDICADORES ECONÓMICOS", estilo_header)]],
        colWidths=[17*cm]
    )

    header.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),colors.HexColor("#2E6E4E")),
        ("ALIGN",(0,0),(-1,-1),"CENTER"),
        ("TOPPADDING",(0,0),(-1,-1),8),
        ("BOTTOMPADDING",(0,0),(-1,-1),8),
    ]))

    elementos.append(header)
    elementos.append(Spacer(1,15))

    # ================= TEXTO
    texto = """
Los siguientes indicadores económicos fueron tomados del Instituto Nacional de Estadística y Geografía.
"""
    elementos.append(Paragraph(texto, estilo_texto))
    elementos.append(Spacer(1,10))

    # ================= SALARIO MÍNIMO
    elementos.append(Paragraph("<b>Salario mínimo</b>", estilo_sub))
    elementos.append(Spacer(1,6))

    texto_sm = """
Establecidos por la Comisión Nacional de los Salarios Mínimos mediante resolución publicada en el Diario Oficial de la Federación del <b>1 de diciembre de 2024</b>. Vigentes a partir del <b>1 de enero de 2025</b>.
"""
    elementos.append(Paragraph(texto_sm, estilo_texto))
    elementos.append(Spacer(1,10))

    tabla_sm = Table([
        ["Área geográfica","Año","Pesos"],
        ["Única","2025","$278.80"],
        ["","2024","$248.93"]
    ], colWidths=[6*cm,5*cm,6*cm])

    tabla_sm.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#2E6E4E")),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("ALIGN",(0,0),(-1,-1),"CENTER"),
        ("GRID",(0,0),(-1,-1),0.5,colors.black)
    ]))

    elementos.append(tabla_sm)
    elementos.append(Spacer(1,15))

    # ================= UMA
    elementos.append(Paragraph("<b>Unidad de medida y actualización (UMA)</b>", estilo_sub))
    elementos.append(Spacer(1,6))

    texto_uma = """
La Unidad de Medida y Actualización es la referencia económica en pesos para determinar la cuantía del pago de las obligaciones y supuestos previstos en las leyes federales.

El valor mensual de la UMA se calcula multiplicando su valor diario por 30.4 veces y su valor anual se calcula multiplicando su valor mensual por 12.
"""
    elementos.append(Paragraph(texto_uma, estilo_texto))
    elementos.append(Spacer(1,10))

    tabla_uma = Table([
        ["Año","Diario","Mensual","Anual"],
        ["2025","$113.14","$3,439.46","$41,273.52"],
        ["2024","$108.57","$3,300.53","$39,606.36"]
    ], colWidths=[4*cm]*4)

    tabla_uma.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#2E6E4E")),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("ALIGN",(0,0),(-1,-1),"CENTER"),
        ("GRID",(0,0),(-1,-1),0.5,colors.black)
    ]))

    elementos.append(tabla_uma)
    elementos.append(Spacer(1,15))

    # ================= DESEMPLEO
    elementos.append(Paragraph("<b>Tasa de desocupación total</b>", estilo_sub))
    elementos.append(Spacer(1,6))

    elementos.append(Paragraph(
        "Porcentaje respecto a la población económicamente activa.",
        estilo_texto
    ))

    elementos.append(Spacer(1,10))

    tabla_des = Table([
        ["Tasa de desocupación en Yucatán","Porcentaje"],
        ["No disponible en el INEGI al cierre del estudio",""]
    ], colWidths=[12*cm,5*cm])

    tabla_des.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#2E6E4E")),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("GRID",(0,0),(-1,-1),0.5,colors.black)
    ]))

    elementos.append(tabla_des)
    elementos.append(Spacer(1,15))

    # ================= INFLACIÓN
    tabla_inf = Table([
        ["Inflación de Diciembre 2024 a Marzo 2025"],
        ["0.88 %, tasa promedio mensual 0.29 %"]
    ], colWidths=[17*cm])

    tabla_inf.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#2E6E4E")),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("ALIGN",(0,0),(-1,-1),"CENTER"),
        ("GRID",(0,0),(-1,-1),0.5,colors.black)
    ]))

    elementos.append(tabla_inf)