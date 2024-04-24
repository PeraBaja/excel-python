import numpy as np
from Intervalo import Intervalo

class Intervalos:
    def __init__(self, datos, cantidadDeIntervalos, redondearAbajo) -> None:
        self.__datos: tuple = datos
        self.__redondearAbajo = redondearAbajo
        self.__cantidadDeIntervalos = cantidadDeIntervalos
        self.__anchoClase = self.__calcular_anchoClase()
        self.__intervalos = self.__agrupar() 
        self.__frecuenciasAbsolutas = self.__calcular_frecuenciasAbsolutas()
        self.__frecuenciasRelativas = self.__calcular_frecuenciasRelativas()
        self.__frecuenciasAcumuladas = self.__calcular_frecuenciasAcumuladas()
        self.__indice = 0
    frecuenciasAbsolutas = property(lambda self: self.__frecuenciasAbsolutas)
    anchoClase = property(lambda self: self.__anchoClase)
    frecuenciasRelativas = property(lambda self: self.__frecuenciasRelativas)
    frecuenciasAcumuladas = property(lambda self: self.__frecuenciasAcumuladas)
    
    def __agrupar(self) -> tuple:
        intervalos = []
        for i in np.arange(min(self.__datos), max(self.__datos), self.__anchoClase):
            intervalos.append(Intervalo(i, i + self.__anchoClase))
        return tuple(intervalos)
    
    def __calcular_anchoClase (self):
        ancho_clase: float = (max(self.__datos) - min(self.__datos)) / self.__cantidadDeIntervalos
        return ancho_clase.__floor__()  if self.__redondearAbajo else ancho_clase.__ceil__()
    
    def __calcular_frecuenciasAbsolutas(self) :
        frecuenciasAbsolutas = []
        for intervalo in self.__intervalos:
            intervalo: Intervalo
            frecuenciasAbsolutas.append(
                sum(1 for dato in self.__datos if intervalo.limiteInferior <= dato < intervalo.limiteSuperior)
                )
        return tuple(frecuenciasAbsolutas)      

    def __calcular_frecuenciasRelativas(self):
        frecuenciasRelativas = []
        for frecuencia in self.frecuenciasAbsolutas: 
            frecuenciasRelativas.append(
                round(frecuencia / len(self.__datos), 2)
                )
        return tuple(frecuenciasRelativas)

    def __calcular_frecuenciasAcumuladas(self):
        frecuenciaAcumulada = 0
        frecuenciasAcumuladas = []
        for frecuenciaAbsoluta in self.frecuenciasAbsolutas:
            frecuenciaAcumulada += frecuenciaAbsoluta
            frecuenciasAcumuladas.append(frecuenciaAcumulada)
        return tuple(frecuenciasAcumuladas)
            
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
                Li = self.__agrupaciones[i].limiteInferior
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
                Li = self.__agrupaciones[i].limiteInferior
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
        if self.__indice < len(self.__agrupaciones):
            intervalo = self.__agrupaciones[self.__indice]
            self.__indice += 1
            return intervalo
        else:
            self.__indice = 0 
            raise StopIteration
    def __str__(self) -> str:
        intervalos = 'Intervalos: fi | Fi \n'
        for i in range(len(self.__agrupaciones)):
            intervalos += f'{self.__agrupaciones[i]}: {self.frecuenciasAbsolutas[i]} | {self.frecuenciasAcumuladas[i]} \n'
        return intervalos