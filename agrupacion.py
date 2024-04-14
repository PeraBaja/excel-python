import numpy as np
from Intervalo import Intervalo 

def agrupar(datos: list, anchoClase: float) -> tuple:
    intervalos = []
    for i in np.arange(min(datos), max(datos), anchoClase):
        intervalos.append(Intervalo(i, i + anchoClase, datos))
    return intervalos

def calcularAnchoClase (valorMinimo, valorMaximo, numeroDeAgrupaciones, redondearAbajo):
    ancho_clase: float = (valorMaximo - valorMinimo) / numeroDeAgrupaciones
    return ancho_clase.__floor__()  if redondearAbajo else ancho_clase.__ceil__()

