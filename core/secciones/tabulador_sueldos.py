from reportlab.platypus import PageBreak, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import cm


# =========================
# FORMATO DINERO
# =========================
def formato_moneda(valor):
    try:
        numero = float(str(valor).replace(",", ""))
        return "${:,.2f}".format(numero)
    except:
        return valor


# =========================
# PREPARAR DATOS
# =========================
def preparar_datos(datos_tabla):

    datos_formateados = []

    for fila in datos_tabla:

        nueva = fila.copy()

        # Columnas de dinero
        nueva[3] = formato_moneda(nueva[3])
        nueva[4] = formato_moneda(nueva[4])
        nueva[5] = formato_moneda(nueva[5])

        datos_formateados.append(nueva)

    return datos_formateados


# =========================
# CREAR TABLA
# =========================
def crear_tabla(data):

    tabla = Table(
        data,
        colWidths=[
            1.5*cm, 3*cm, 6*cm,
            2.5*cm, 2.5*cm, 2.5*cm,
            1.8*cm, 2.5*cm, 2.5*cm, 2.5*cm, 2.5*cm
        ],
        repeatRows=2
    )

    estilo = [

        # HEADER
        ("BACKGROUND", (0,0), (-1,1), colors.HexColor("#2f6f4f")),
        ("TEXTCOLOR", (0,0), (-1,1), colors.white),
        ("FONTNAME", (0,0), (-1,1), "Helvetica-Bold"),

        # GRID
        ("GRID", (0,0), (-1,-1), 0.25, colors.black),

        # ALIGN
        ("ALIGN", (0,0), (-1,-1), "CENTER"),

    ]

    # 🔥 ZEBRA STYLE
    for i in range(2, len(data)):
        if i % 2 == 0:
            estilo.append(("BACKGROUND", (0,i), (-1,i), colors.whitesmoke))

    tabla.setStyle(TableStyle(estilo))

    return tabla


# =========================
# PAGINA TABULADOR
# =========================
def pagina_tabulador_sueldos(elementos, datos_tabla):

    estilo_titulo = ParagraphStyle(
        "titulo",
        fontSize=14,
        alignment=TA_CENTER
    )

    datos_tabla = preparar_datos(datos_tabla)

    # HEADERS
    header1 = [
        "Clave", "Área", "Puesto Homologado",
        "Sueldos Mensuales", "", "",
        "Perfil del Puesto", "", "", "", ""
    ]

    header2 = [
        "", "", "",
        "Base Contratación", "Sueldo Neto", "Sueldo Integrado",
        "No. Emp.", "Escolaridad", "Experiencia", "Idioma", "Tipo"
    ]

    # =========================
    # DIVIDIR EN BLOQUES
    # =========================
    filas_por_pagina = 25

    bloques = [
        datos_tabla[i:i + filas_por_pagina]
        for i in range(0, len(datos_tabla), filas_por_pagina)
    ]

    for i, bloque in enumerate(bloques):

        elementos.append(PageBreak())

        # SOLO primer página muestra título
        if i == 0:
            elementos.append(Paragraph(
                "TABULADOR DE SUELDOS",
                estilo_titulo
            ))
            elementos.append(Spacer(1, 15))

        data = [header1, header2] + bloque

        tabla = crear_tabla(data)

        elementos.append(tabla)