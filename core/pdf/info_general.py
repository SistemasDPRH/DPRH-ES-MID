from reportlab.platypus import Paragraph, Spacer, PageBreak, Image, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.lib.units import cm


def pagina_info_general(elementos):

    estilo_header = ParagraphStyle(
        "header", fontSize=12, alignment=TA_CENTER, textColor=colors.white
    )

    estilo_texto = ParagraphStyle(
        "texto", fontSize=10, alignment=TA_JUSTIFY, leading=14
    )

    # =========================
    # PÁGINA 1
    # =========================
    elementos.append(PageBreak())

    header = Table(
        [[Paragraph("INFORMACIÓN GENERAL DE LA ENCUESTA", estilo_header)]],
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

    texto = """
<b>Fecha de los datos de la muestra.</b><br/>
Los datos encuestados en la presente investigación fueron recolectados hasta abril 2025 y representan las condiciones laborales de cada empresa durante el presente año.

<br/><br/>

<b>Tamaño de la muestra.</b><br/>
El número total de empleados de la muestra es de 26,960. El número de empleados no Sindicalizados es de 16,799 y el de Sindicalizados es de 10,161 siendo de 1348 el promedio de trabajadores por empresa.

El número de puestos y el total de empleados utilizado para los cálculos estadísticos depende de que cada puesto sea reportado por más de una empresa. En el presente estudio el Total de Puestos es de 236 y el Total de Empleados es de 14,855.

<br/><br/>
La siguiente gráfica representa el total de empleados y su distribución sindical.
"""

    elementos.append(Paragraph(texto, estilo_texto))
    elementos.append(Spacer(1,10))

    # GRÁFICA 1
    try:
        img = Image("assets/grafica_sindical.png", width=16*cm, height=9*cm)
        img.hAlign = "CENTER"
        elementos.append(img)
    except:
        elementos.append(Spacer(1,50))

    elementos.append(Spacer(1,10))

    texto2 = """
<b>Distribución de empleados</b><br/>
El número de personal empleado está distribuido de la siguiente manera:

<br/><br/>
Porcentaje de empresas con:<br/>
Número de empleados menor o igual a 400 ............................................... Rango 1: 45.00%<br/>
Número de empleados mayor que 400 y menor o igual a 900 ............ Rango 2: 30.00%<br/>
Número de empleados mayor que 900 y menor o igual a 9100 ......... Rango 3: 25.00%
"""
    elementos.append(Paragraph(texto2, estilo_texto))

    elementos.append(Spacer(1,10))

    # GRÁFICA 2
    try:
        img2 = Image("assets/grafica_rangos.png", width=16*cm, height=9*cm)
        img2.hAlign = "CENTER"
        elementos.append(img2)
    except:
        elementos.append(Spacer(1,50))

    # =========================
    # PÁGINA 2 (ROTACIÓN)
    # =========================
    elementos.append(PageBreak())

    texto_rotacion = """
<b>Índice de Rotación de personal.</b><br/><br/>

Las empresas participantes reportan una rotación media anual del <b>40.68%</b> dentro de un rango de <b>3.54%</b> la de menor rotación a <b>116.50%</b> la de mayor.

<br/><br/>

<b>Índice de Separación:</b> Tiempo de permanencia de empleados de Nuevo Ingreso

<br/><br/>
Los resultados obtenidos según la muestra encuestada fueron los siguientes:

<br/><br/>

<b>Menor o igual a 30 días:</b> Rotación media del <b>30.84%</b> dentro de un rango de <b>5.00%</b> la de menor rotación a <b>98.00%</b> la de mayor.

<br/><br/>

<b>Mayor a 30 y menor o igual a 90 días:</b> Rotación media del <b>32.92%</b> dentro de un rango de <b>9.00%</b> la de menor rotación a <b>96.00%</b> la de mayor.

<br/><br/>

<b>Mayor a 90 y menor o igual a 180 días:</b> Rotación media del <b>30.22%</b> dentro de un rango de <b>4.00%</b> la de menor rotación a <b>100.00%</b> la de mayor.
"""

    elementos.append(Paragraph(texto_rotacion, estilo_texto))