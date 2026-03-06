from core.lector_empresas import cargar_empresas


empresas = cargar_empresas("merida2026")

print("Empresas cargadas:", len(empresas))

for e in empresas:

    print(e["nombre"])
    print("filas excel:", len(e["sueldos"]))