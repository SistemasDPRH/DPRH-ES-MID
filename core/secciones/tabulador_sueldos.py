from reportlab.platypus import Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm


def formato_moneda(valor):
    try:
        return "${:,.2f}".format(valor)
    except:
        return "$0.00"


def construir_fila(nombre, stats):

    if not stats:
        return [nombre] + ["-"] * 8

    return [
        nombre,
        formato_moneda(stats["min"]),
        formato_moneda(stats["q1"]),
        formato_moneda(stats["mediana"]),
        formato_moneda(stats["q3"]),
        formato_moneda(stats["max"]),
        formato_moneda(stats["media"]),
        formato_moneda(stats["media_ponderada"]),
        formato_moneda(stats["std"]),
    ]


def pagina_tabulador_sueldos(elementos, tabulador):

    estilo_titulo = ParagraphStyle(
        name="titulo",
        alignment=TA_CENTER,
        fontSize=14
    )

    elementos.append(PageBreak())
    elementos.append(Paragraph("VIII.- Evaluación Comparativa de Sueldos", estilo_titulo))
    elementos.append(Spacer(1, 20))

    for item in tabulador:

        # =========================
        # ENCABEZADO VERDE
        # =========================
        encabezado = Table(
            [[f"Puesto: {item['puesto']}"]],
            colWidths=[17*cm]
        )

        encabezado.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), colors.darkgreen),
            ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 11),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ]))

        elementos.append(encabezado)
        elementos.append(Spacer(1, 6))

        # =========================
        # TABLA PRINCIPAL
        # =========================
        tabla_data = [
            [
                "Tipo",
                "Mínimo",
                "Inferior",
                "Mediana",
                "Superior",
                "Máximo",
                "Media",
                "Media Pond.",
                "Desv. Std"
            ],
            construir_fila("Base", item["base"]),
            construir_fila("Neto", item["neto"]),
            construir_fila("Integrado", item["integrado"]),
        ]

        tabla = Table(tabla_data, repeatRows=1)

        tabla.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.green),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 8),

            ("GRID", (0, 0), (-1, -1), 0.5, colors.black),

            ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
            ("ALIGN", (0, 0), (0, -1), "LEFT"),
        ]))

        elementos.append(tabla)
        elementos.append(Spacer(1, 10))

        # =========================
        # TABLA PERFIL (simplificada)
        # =========================
        detalle = item["detalle"]

        if detalle:

            perfil_data = [
                ["Empresa", "Escolaridad", "Experiencia", "Idioma", "Tipo"]
            ]

            for d in detalle[:5]:  # limitar para que no rompa diseño
                perfil_data.append([
                    d.get("empresa", ""),
                    d.get("escolaridad", ""),
                    d.get("experiencia", ""),
                    d.get("idioma", ""),
                    d.get("tipo_puesto", ""),
                ])

            tabla_perfil = Table(perfil_data)

            tabla_perfil.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.black),
                ("FONTSIZE", (0, 0), (-1, -1), 7),
            ]))

            elementos.append(tabla_perfil)

        elementos.append(Spacer(1, 25))