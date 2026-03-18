from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm

from core.procesador_estadisticas import porcentaje, promedio
from core.graficas.grafica_prestaciones import grafica_si_no


def pagina_prestaciones(elementos, empresas):

    estilo_header = ParagraphStyle(
        "header", fontSize=13, alignment=TA_CENTER
    )

    elementos.append(PageBreak())

    elementos.append(Paragraph(
        "VI. PRESTACIONES Y BENEFICIOS",
        estilo_header
    ))

    elementos.append(Spacer(1,20))

    # =========================
    # 1. SEGURO DE VIDA
    # =========================
    tabla = Table([
        ["Seguro de Vida", "%"],
        ["Ejecutivos", f"{porcentaje(empresas,'SeguroVidaEjecutivosSi')}%"],
        ["No Sindicalizados", f"{porcentaje(empresas,'SeguroVidaNoSindSi')}%"],
        ["Sindicalizados", f"{porcentaje(empresas,'SeguroVidaSindSi')}%"],
    ], colWidths=[10*cm,5*cm])

    tabla.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),0.5,colors.grey),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
    ]))

    elementos.append(tabla)
    elementos.append(Spacer(1,15))

    ruta = "temp_seguro_vida.png"
    grafica_si_no(empresas,"SeguroVidaEjecutivosSi","SeguroVidaEjecutivosNo","Seguro Vida Ejecutivos",ruta)

    elementos.append(Image(ruta, width=8*cm, height=8*cm))

    elementos.append(Spacer(1,25))

    # =========================
    # 2. GASTOS MÉDICOS
    # =========================
    tabla2 = Table([
        ["Gastos Médicos Mayores", "%"],
        ["Ejecutivos", f"{porcentaje(empresas,'GastosMedicosEjecutivos')}%"],
        ["No Sindicalizados", f"{porcentaje(empresas,'GastosMedicosNoSind')}%"],
        ["Sindicalizados", f"{porcentaje(empresas,'GastosMedicosSind')}%"],
    ], colWidths=[10*cm,5*cm])

    tabla2.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),0.5,colors.grey),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
    ]))

    elementos.append(tabla2)
    elementos.append(Spacer(1,25))

    # =========================
    # 3. FONDO DE AHORRO
    # =========================
    tabla3 = Table([
        ["Fondo de Ahorro", "%"],
        ["Ejecutivos", f"{porcentaje(empresas,'FondoDeAhorroEjecutivosSi')}%"],
        ["No Sindicalizados", f"{porcentaje(empresas,'FondoDeAhorroNoSindSi')}%"],
        ["Sindicalizados", f"{porcentaje(empresas,'FondoDeAhorroSindSi')}%"],
    ], colWidths=[10*cm,5*cm])

    tabla3.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),0.5,colors.grey),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
    ]))

    elementos.append(tabla3)
    elementos.append(Spacer(1,25))

    # =========================
    # 4. VALES DESPENSA
    # =========================
    tabla4 = Table([
        ["Vales de Despensa", "%"],
        ["Empresas que otorgan", f"{porcentaje(empresas,'ValesDespensaSi')}%"],
    ], colWidths=[10*cm,5*cm])

    tabla4.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),0.5,colors.grey),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
    ]))

    elementos.append(tabla4)
    elementos.append(Spacer(1,25))

    # =========================
    # 5. BONOS
    # =========================
    tabla5 = Table([
        ["Bonos por metas", "%"],
        ["Ejecutivos", f"{porcentaje(empresas,'BonoMetasEjecutivosSi')}%"],
        ["No Sindicalizados", f"{porcentaje(empresas,'BonoMetasNoSindSi')}%"],
        ["Sindicalizados", f"{porcentaje(empresas,'BonoMetasSindSi')}%"],
    ], colWidths=[10*cm,5*cm])

    tabla5.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),0.5,colors.grey),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
    ]))

    elementos.append(tabla5)
    elementos.append(Spacer(1,25))

    # =========================
    # 6. TRANSPORTE
    # =========================
    tabla6 = Table([
        ["Apoyo de Transporte", "%"],
        ["Empresas que otorgan", f"{porcentaje(empresas,'AyudaTransporteSi')}%"],
    ], colWidths=[10*cm,5*cm])

    tabla6.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),0.5,colors.grey),
        ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),
    ]))

    elementos.append(tabla6)