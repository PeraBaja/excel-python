import numpy as np
from estadistica_facil.Intervalo import Intervalo


        
def agrupar(datos: tuple, ancho_clase) -> tuple:
    """_Crea una tupla de intervalos_

    Args:
        datos (tuple) 
        ancho_clase (int): _La cantidad de divisiones que se harán a los datos_
        redondearAbajo (bool): _Si al calcular el ancho de clase se redondea hacia abajo_
    """
    intervalos = []
    try:
        for i in np.arange(min(datos), max(datos), ancho_clase):
            intervalos.append(Intervalo(i, i + ancho_clase))
    except ZeroDivisionError:
        print("❌ Error al tratar de crear los intervalos. El ancho de clase debe ser mayor o igual a 1")
    else:
        return tuple(intervalos)

def calcular_anchoClase(datos, cantidadDeIntervalos: int, redondearAbajo: bool):       
    ancho_clase: float = (max(datos) - min(datos)) / cantidadDeIntervalos
    return ancho_clase.__floor__()  if redondearAbajo else ancho_clase.__ceil__()
