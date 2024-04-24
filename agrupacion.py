import numpy as np
from Intervalo import Intervalo

class Agrupacion:
    def __init__(self, datos, cantidadDeIntervalos, redondearAbajo) -> None:
        self.__datos: tuple = datos
        self.__redondearAbajo = redondearAbajo
        self.__cantidadDeIntervalos = cantidadDeIntervalos
        self.__anchoClase = self.__calcular_anchoClase()
        self.__intervalos = self.__agrupar() 
        self.__indice = 0
    def __agrupar(self) -> tuple:
        intervalos = []
        for i in np.arange(min(self.__datos), max(self.__datos), self.__anchoClase):
            intervalos.append(Intervalo(i, i + self.__anchoClase))
        return tuple(intervalos)
    
    def __calcular_anchoClase (self):
        ancho_clase: float = (max(self.__datos) - min(self.__datos)) / self.__cantidadDeIntervalos
        return ancho_clase.__floor__()  if self.__redondearAbajo else ancho_clase.__ceil__()
            
    def media(self):
        resultado = [intervalo.marcaClase * Fi for intervalo, Fi in zip(self.__agrupaciones, self.frecuenciasAbsolutas)]
        return round(sum(resultado) / len(self.__datos), 2)

    def mediana(self):
        Me = sum(self.frecuenciasAbsolutas) / 2
        FiAnterior = 0
        fi = 0
        Li = 0
        for i in range(len(self.frecuenciasAcumuladas)):
            if self.frecuenciasAcumuladas[i] > Me:
                try:
                    FiAnterior = self.frecuenciasAcumuladas[i - 1]
                except IndexError:
                    FiAnterior = 0
                fi = self.frecuenciasAbsolutas[i]
                Li = self.__intervalos[i].limiteInferior
                break
        return round(Li + ((Me - FiAnterior) / fi)* self.anchoClase, 2)
    
    def moda(self):
        Mo = 0
        fi = 0
        fiAnterior = 0
        fiPosterior = 0
        Li = 0
        for i in range(len(self.frecuenciasAbsolutas)):
            if self.frecuenciasAbsolutas[i] > Mo:
                Mo = self.frecuenciasAbsolutas[i]
                fi = self.frecuenciasAbsolutas[i]
                Li = self.__intervalos[i].limiteInferior
                try:
                    fiAnterior = self.frecuenciasAbsolutas[i - 1]
                except IndexError:
                    fiAnterior = 0
                try:
                    fiPosterior = self.frecuenciasAbsolutas[i + 1]
                except IndexError:
                    fiPosterior = 0
        return round(Li + ((Mo - fiAnterior) / (fi - fiAnterior + fi - fiPosterior))* self.anchoClase, 2)
    
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
        intervalos = 'Intervalos: fi | Fi \n'
        for i in range(len(self.__intervalos)):
            intervalos += f'{self.__intervalos[i]}: {self.frecuenciasAbsolutas[i]} | {self.frecuenciasAcumuladas[i]} \n'
        return intervalos