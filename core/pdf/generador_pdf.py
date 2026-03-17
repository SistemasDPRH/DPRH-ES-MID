from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter

from core.pdf.portada import generar_portada
from core.pdf.tabla_contenido import pagina_tabla_contenido
from core.pdf.objetivo import pagina_objetivo
from core.pdf.caracteristicas import pagina_caracteristicas_encuesta


def generar_pdf(nombre_archivo, mes, anio, datos):

    pdf = SimpleDocTemplate(nombre_archivo, pagesize=letter)

    elementos = []

    generar_portada(elementos, mes, anio)
    pagina_tabla_contenido(elementos)
    pagina_objetivo(elementos)
    pagina_caracteristicas_encuesta(elementos, datos)

    pdf.build(elementos)