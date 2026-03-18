from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm

from core.graficas.grafica_salarios import grafica_salarios


def calcular_distribucion(empresas):

    # ⚠️ SIMULADO (luego conectamos con Excel)
    total = sum(
        int(e.get("NumeroEmpleadosNoSind",0) or 0) +
        int(e.get("NumeroEmpleadosSind",0) or 0)
        for e in empresas
    )

    return {
        "1 SM": int(total * 0.10),
        "2 SM": int(total * 0.25),
        "3 SM": int(total * 0.30),
        "4 SM": int(total * 0.20),
        "5+ SM": int(total * 0.15),
    }


def pagina_salarios(elementos, empresas):

    estilo_header = ParagraphStyle(
        "header", fontSize=13, alignment=TA_CENTER
    )

    elementos.append(PageBreak())

    elementos.append(Paragraph(
        "VII. SALARIOS MÍNIMOS",
        estilo_header
    ))

    elementos.append(Spacer(1,20))

    distribucion = calcular_distribucion(empresas)

    # =========================
    # TABLA
    # =========================
    data = [["Rango", "Número de empleados"]]

    for k, v in distribucion.items():
        data.append([k, v])

    tabla = Table(data, colWidths=[8*cm,7*cm])

    tabla.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),0.5,colors.grey),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
        ("ALIGN",(1,1),(-1,-1),"CENTER"),
    ]))

    elementos.append(tabla)
    elementos.append(Spacer(1,20))

    # =========================
    # GRÁFICA
    # =========================
    ruta = "temp_salarios.png"
    grafica_salarios(distribucion, ruta)

    elementos.append(Image(ruta, width=12*cm, height=8*cm))

    elementos.append(Spacer(1,25))

    # =========================
    # TABLA DE PUESTOS (placeholder)
    # =========================
    tabla2 = Table([
        ["Puesto", "Rango Salarial"],
        ["Administrador", "3 SM"],
        ["Operador", "2 SM"],
        ["Gerente", "5+ SM"],
    ], colWidths=[8*cm,7*cm])

    tabla2.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),0.5,colors.grey),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
    ]))

    elementos.append(tabla2)