from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.units import cm
from reportlab.lib import colors


def pagina_caracteristicas_encuesta(elementos, datos):

    # =========================
    # ESTILOS
    # =========================
    estilo_header = ParagraphStyle(
        "header",
        fontSize=12,
        alignment=TA_CENTER,
        textColor=colors.white
    )

    estilo_texto = ParagraphStyle(
        "texto",
        fontSize=10,
        alignment=TA_JUSTIFY,
        leading=14
    )

    estilo_subtitulo = ParagraphStyle(
        "subtitulo",
        fontSize=11,
        alignment=TA_LEFT,
        textColor=colors.white
    )

    elementos.append(PageBreak())

    # =========================
    # HEADER VERDE
    # =========================
    header = Table(
        [[Paragraph("CARACTERÍSTICAS DE LA ENCUESTA", estilo_header)]],
        colWidths=[17*cm]
    )

    header.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#2E6E4E")),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))

    elementos.append(header)
    elementos.append(Spacer(1,15))

    # =========================
    # TEXTO PRINCIPAL
    # =========================
    texto = f"""
En el presente estudio participaron <b>{datos["empresas"]} empresas</b> ubicadas del estado de Yucatán.

El número de puestos reportados simultáneamente por al menos dos empresas fue de <b>{datos["puestos"]}</b>; 
con un total de <b>{datos["empleados"]}</b> empleados asociados a esos puestos.
"""

    elementos.append(Paragraph(texto, estilo_texto))
    elementos.append(Spacer(1,20))

    # =========================
    # SUBTITULO EMPRESAS
    # =========================
    subtitulo = Table(
        [[Paragraph("Empresas participantes", estilo_subtitulo)]],
        colWidths=[17*cm]
    )

    subtitulo.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#2E6E4E")),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))

    elementos.append(subtitulo)
    elementos.append(Spacer(1,10))

    # =========================
    # LISTA DE EMPRESAS
    # =========================
    empresas = [
        ["• AEI","• Baldesigns de México"],
        ["• Bohn de México","• Dimadera"],
        ["• Dunosusa","• Elemetic"],
        ["• Empaques Nova","• Grupo Crio"],
        ["• Industria Salinera de Yucatán","• Kekén"],
        ["• La Anita","• La Lupita"],
        ["• Marbol","• Millet Industria de Vidrio"],
        ["• Milsco de México","• Momente Brands"],
        ["• Provi","• Stuller México"],
        ["• The Palace Company","• Uchiyama Manufacturing"]
    ]

    tabla = Table(empresas, colWidths=[8.5*cm,8.5*cm])

    tabla.setStyle(TableStyle([
        ("FONTSIZE",(0,0),(-1,-1),10),
        ("BOTTOMPADDING",(0,0),(-1,-1),4),
    ]))

    elementos.append(tabla)
    elementos.append(Spacer(1,20))

    # =========================
    # SUBTITULO GRÁFICA
    # =========================
    subtitulo2 = Table(
        [[Paragraph("Representación gráfica por sectores de las empresas", estilo_subtitulo)]],
        colWidths=[17*cm]
    )

    subtitulo2.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#2E6E4E")),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ]))

    elementos.append(subtitulo2)
    elementos.append(Spacer(1,10))

    # =========================
    # GRÁFICA
    # =========================
    try:
        grafica = Image("assets/grafica_sectores.png", width=16*cm, height=9*cm)
        grafica.hAlign = "CENTER"
        elementos.append(grafica)
    except:
        elementos.append(Paragraph("<< Gráfica pendiente >>", estilo_texto))