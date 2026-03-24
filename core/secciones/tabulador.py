from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm
from core.utils_format import formato_moneda

from core.procesador_estadisticas import porcentaje, promedio

from reportlab.platypus import Image
from core.graficas.grafica_tabulador import grafica_contrato_colectivo

def tabla_estilo(tabla):
    tabla.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.grey),
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("ALIGN",(1,1),(-1,-1),"CENTER"),
        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
    ]))
    return tabla


def pagina_tabulador(elementos, datos):

    elementos.append(PageBreak())

    estilo = ParagraphStyle(name="titulo", alignment=TA_CENTER, fontSize=14)

    elementos.append(Paragraph("Estudio Comparativo de Sueldos", estilo))
    elementos.append(Spacer(1, 20))

    for item in datos:

        # ENCABEZADO VERDE
        encabezado = [
            ["Puesto:", item["puesto"]]
        ]

        t_enc = Table(encabezado, colWidths=[4*cm, 12*cm])
        t_enc.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.darkgreen),
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ]))

        elementos.append(t_enc)
        elementos.append(Spacer(1, 10))

        # TABLA PRINCIPAL
        tabla_data = [
            ["", "Mínimo", "Inferior", "Mediana", "Superior", "Máximo", "Media", "Desv. Std"],
            [
                "Sueldo",
                formato_moneda(item["min"]),
                formato_moneda(item["q1"]),
                formato_moneda(item["mediana"]),
                formato_moneda(item["q3"]),
                formato_moneda(item["max"]),
                formato_moneda(item["media"]),
                formato_moneda(item["std"])
            ]
        ]

        tabla = Table(tabla_data)

        tabla.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.green),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
            ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
        ]))

        elementos.append(tabla)
        elementos.append(Spacer(1, 25))