from datetime import datetime

MESES = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

def fecha_a_mes_anio(fecha):

    # formato esperado dd/mm/aa o dd/mm/yyyy
    f = datetime.strptime(fecha, "%d/%m/%y")

    mes = MESES[f.month]
    anio = f.year

    return f"{mes} {anio}"