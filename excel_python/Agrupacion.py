import numpy as np
from .Intervalo import Intervalo

class Agrupacion:
    def __init__(self, datos: tuple, cantidadDeIntervalos: int, redondearAbajo: bool) -> None:
        """_Crea una tupla de intervalos_

        Args:
            datos (tuple) 
            cantidadDeIntervalos (int): _La cantidad de divisiones que se harán a los datos_
            redondearAbajo (bool): _Si al calcular el ancho de clase se redondea hacia abajo_
        """
        self.__datos: tuple = datos
        self.__redondearAbajo = redondearAbajo
        self.__cantidadDeIntervalos = cantidadDeIntervalos
        self.__anchoClase = self.__calcular_anchoClase()
        self.__intervalos = self.__agrupar() 
        self.__indice = 0
    anchoClase = property(lambda self: self.__anchoClase)     
    intervalos = property(lambda self: self.__intervalos)
    def __agrupar(self) -> tuple:
        intervalos = []
        for i in np.arange(min(self.__datos), max(self.__datos), self.__anchoClase):
            intervalos.append(Intervalo(i, i + self.__anchoClase))
        return tuple(intervalos)
    
    def __calcular_anchoClase (self):
        ancho_clase: float = (max(self.__datos) - min(self.__datos)) / self.__cantidadDeIntervalos
        return ancho_clase.__floor__()  if self.__redondearAbajo else ancho_clase.__ceil__()
            
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice < len(self.__intervalos):
            intervalo = self.__intervalos[self.__indice]
            self.__indice += 1
            return intervalo
        else:
            self.__indice = 0 
            raise StopIteration
    def __str__(self) -> str:
        intervalos = 'Intervalos:\n'
        for i in range(len(self.__intervalos)):
            intervalos += f'{self.__intervalos[i]}:\n'
        return intervalos