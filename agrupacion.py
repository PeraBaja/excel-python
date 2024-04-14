import numpy as np
from Intervalo import Intervalo 
class Agrupaciones:
    def __init__(self, datos, cantidadDeAgrupaciones, redondearAbajo) -> None:
        self.__datos = datos
        self.__redondearAbajo = redondearAbajo
        self.__cantidadDeAgrupaciones = cantidadDeAgrupaciones
        anchoClase = self.__calcularAnchoClase(min(datos), max(datos))
        self.__agrupaciones = self.__agrupar(datos)
    
    
    def __agrupar(datos: list, anchoClase: float) -> tuple:
        intervalos = []
        for i in np.arange(min(datos), max(datos), anchoClase):
            intervalos.append(Intervalo(i, i + anchoClase))
        return tuple(intervalos)

    def __calcularAnchoClase (self, valorMinimo, valorMaximo):
        ancho_clase: float = (valorMaximo - valorMinimo) / self.__cantidadDeAgrupaciones
        return ancho_clase.__floor__()  if self.__redondearAbajo else ancho_clase.__ceil__()

    def frecuenciasAbsolutas(self) :
        for intervalo in self.__agrupaciones:
            frecuenciaAbsoluta = sum(1 for dato in self.__datos if intervalo.limiteInferior <= dato < intervalo.limiteSuperior)
            return frecuenciaAbsoluta

    def frecuenciaRelativa(self):
        return round(self.frecuenciaAbsoluta() / len(self.__datos), 2)
