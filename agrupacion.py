import numpy as np
from Intervalo import Intervalo 
class Agrupaciones:
    def __init__(self, datos, cantidadDeAgrupaciones, redondearAbajo) -> None:
        self.__datos = datos
        self.__redondearAbajo = redondearAbajo
        self.__cantidadDeAgrupaciones = cantidadDeAgrupaciones
        self.__anchoClase = self.anchoClase
        self.__agrupaciones = self.__agrupar()
    
    
    def __agrupar(self) -> tuple:
        intervalos = []
        for i in np.arange(min(self.__datos), max(self.__datos), self.__anchoClase):
            intervalos.append(Intervalo(i, i + self.__anchoClase))
        return tuple(intervalos)
    
    @property
    def anchoClase (self):
        ancho_clase: float = (max(self.__datos) - min(self.__datos)) / self.__cantidadDeAgrupaciones
        return ancho_clase.__floor__()  if self.__redondearAbajo else ancho_clase.__ceil__()

    @property
    def frecuenciasAbsolutas(self) :
        frecuenciasAbsolutas = []
        for intervalo in self.__agrupaciones:
            intervalo: Intervalo
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
    
    def __str__(self) -> str:
        intervalos = ''
        for intervalo in self.__agrupaciones:
            intervalos += f'{intervalo}, '
        return intervalos