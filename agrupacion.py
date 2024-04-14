import numpy as np
from Intervalo import Intervalo 
class Agrupaciones:
    def __init__(self, datos, cantidadDeAgrupaciones, redondearAbajo) -> None:
        self.__datos = datos
        self.__redondearAbajo = redondearAbajo
        self.__cantidadDeAgrupaciones = cantidadDeAgrupaciones
        self.__anchoClase = self.anchoClase
        self.__agrupaciones = self.__agrupar(datos, self.__anchoClase)
    
    
    def __agrupar(datos: list, anchoClase: float) -> tuple:
        intervalos = []
        for i in np.arange(min(datos), max(datos), anchoClase):
            intervalos.append(Intervalo(i, i + anchoClase))
        return tuple(intervalos)
    
    @property
    def anchoClase (self):
        ancho_clase: float = (max(self.__datos) - min(self.__datos)) / self.__cantidadDeAgrupaciones
        return ancho_clase.__floor__()  if self.__redondearAbajo else ancho_clase.__ceil__()

    @property
    def frecuenciasAbsolutas(self) :
        frecuenciasAbsolutas = []
        for intervalo in self.__agrupaciones:
            frecuenciasAbsolutas.append(
                sum(1 for dato in self.__datos if intervalo.limiteInferior <= dato < intervalo.limiteSuperior)
                )
        return tuple(frecuenciasAbsolutas)    

    @property
    def frecuenciasRelativas(self):
        frecuenciasRelativas = []
        for frecuencia in self.frecuenciasAbsolutas:
            frecuenciasRelativas.append(
                round(frecuencia / len(self.__datos), 2)
                )
        return tuple(frecuenciasRelativas)