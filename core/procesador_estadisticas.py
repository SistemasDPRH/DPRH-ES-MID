def porcentaje(empresas, campo):
    total = len(empresas)
    if total == 0:
        return 0

    count = sum(1 for e in empresas if e.get(campo) == True)
    return round((count / total) * 100, 2)


def promedio(empresas, campo):
    valores = [float(e.get(campo, 0) or 0) for e in empresas if e.get(campo)]
    if not valores:
        return 0
    return round(sum(valores) / len(valores), 2)