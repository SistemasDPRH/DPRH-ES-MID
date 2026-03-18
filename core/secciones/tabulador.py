from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm

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


def pagina_tabulador(elementos, empresas):

    estilo_header = ParagraphStyle(
        "header", fontSize=12, alignment=TA_CENTER, textColor=colors.white
    )

    elementos.append(PageBreak())

    # =========================
    # HEADER
    # =========================
    header = Table(
        [[Paragraph("V. TABULADOR DE SUELDOS Y CONTRATO COLECTIVO", estilo_header)]],
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

    # =========================
    # 1. CONTRATO COLECTIVO
    # =========================
    tabla1 = Table([
        ["Contrato Colectivo", "%"],
        ["Sí", f"{porcentaje(empresas, 'ContratoColectivoSi')}%"],
        ["No", f"{porcentaje(empresas, 'ContratoColectivoNo')}%"],
    ], colWidths=[10*cm, 7*cm])

    elementos.append(tabla_estilo(tabla1))
    elementos.append(Spacer(1,20))

    # =========================
    # 2. TIPO DE SINDICATO
    # =========================
    tabla2 = Table([
        ["Tipo de Sindicato", "%"],
        ["CROC", f"{porcentaje(empresas, 'ContratoColectivoCROC')}%"],
        ["CTM", f"{porcentaje(empresas, 'ContratoColectivoCTM')}%"],
        ["CROM", f"{porcentaje(empresas, 'ContratoColectivoCROM')}%"],
        ["Otro", f"{porcentaje(empresas, 'ContratoColectivoOtro')}%"],
    ], colWidths=[10*cm, 7*cm])

    elementos.append(tabla_estilo(tabla2))
    elementos.append(Spacer(1,20))

    # =========================
    # 3. FRECUENCIA TABULADOR
    # =========================
    tabla3 = Table([
        ["Frecuencia revisión tabulador", "%"],
        ["Cada 3 meses", f"{porcentaje(empresas, 'FrecuenciaRevTabulador3')}%"],
        ["Cada 6 meses", f"{porcentaje(empresas, 'FrecuenciaRevTabulador6')}%"],
        ["Cada 9 meses", f"{porcentaje(empresas, 'FrecuenciaRevTabulador9')}%"],
        ["Cada 12 meses", f"{porcentaje(empresas, 'FrecuenciaRevTabulador12')}%"],
        ["Otro", f"{porcentaje(empresas, 'FrecuenciaRevTabuladorOtro')}%"],
    ], colWidths=[10*cm, 7*cm])

    elementos.append(tabla_estilo(tabla3))
    elementos.append(Spacer(1,20))

    # =========================
    # 4. INCREMENTOS NO SINDICALIZADOS
    # =========================
    tabla4 = Table([
        ["Incrementos No Sindicalizados", "% Promedio"],
        ["Último incremento", f"{promedio(empresas, 'UltimoIncrementoTabuladorPctNoSind')}%"],
        ["Próximo incremento", f"{promedio(empresas, 'ProximoIncrementoTabuladorPctNoSind')}%"],
    ], colWidths=[10*cm, 7*cm])

    elementos.append(tabla_estilo(tabla4))
    elementos.append(Spacer(1,20))

    # =========================
    # 5. ESTRUCTURA TABULADOR
    # =========================
    tabla5 = Table([
        ["Estructura formal de tabulador", "%"],
        ["Sí", f"{porcentaje(empresas, 'EstructuraFormalTabuladorSi')}%"],
        ["No", f"{porcentaje(empresas, 'EstructuraFormalTabuladorNo')}%"],
    ], colWidths=[10*cm, 7*cm])

    elementos.append(tabla_estilo(tabla5))
    elementos.append(Spacer(1,20))

    # =========================
    # 6. SINDICALIZADOS
    # =========================
    tabla6 = Table([
        ["Datos Sindicalizados", "% Promedio"],
        ["Incremento sueldos", f"{promedio(empresas, 'UltimoIncrementoSueldosPctSind')}%"],
        ["Incremento prestaciones", f"{promedio(empresas, 'UltimoIncrementoPrestacionesPctSind')}%"],
    ], colWidths=[10*cm, 7*cm])

    elementos.append(tabla_estilo(tabla6))
    elementos.append(Spacer(1,20))

    # =========================
    # 7. REVISIÓN CONTRATO
    # =========================
    # (aquí no promedio porque es fecha)
    fechas = [e.get("UltimaRevisionCtoColectivoFechaSind") for e in empresas if e.get("UltimaRevisionCtoColectivoFechaSind")]

    fecha_texto = fechas[0] if fechas else "No disponible"

    tabla7 = Table([
        ["Última revisión contrato colectivo"],
        [fecha_texto]
    ], colWidths=[17*cm])

    tabla7.setStyle(TableStyle([
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("ALIGN",(0,0),(-1,-1),"CENTER"),
    ]))

    elementos.append(tabla7)