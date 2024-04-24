from enum import Enum, auto
from Agrupacion import Agrupacion
from Intervalo import Intervalo
class Frecuencias:
    def __init__(self, agrupaciones: Agrupacion, datos: list):
        if type(agrupaciones) == Agrupacion:
            self.__agrupaciones: Agrupacion = agrupaciones
        else:
            print('Error. Debe pasarse como argumento un objeto de tipo agrupación')
            raise TypeError
        self.__datos = datos
        self.__frecuenciasAbsolutas = self.__calcular_frecuenciasAbsolutas()
        self.__frecuenciasRelativas = self.__calcular_frecuenciasRelativas()
        self.__frecuenciasAcumuladas = self.__calcular_frecuenciasAcumuladas()
    
    frecuenciasAbsolutas = property(lambda self: self.__frecuenciasAbsolutas)
    frecuenciasRelativas = property(lambda self: self.__frecuenciasRelativas)
    frecuenciasAcumuladas = property(lambda self: self.__frecuenciasAcumuladas)
        

    def __calcular_frecuenciasAbsolutas(self) :
        frecuenciasAbsolutas = []
        for intervalo in self.__agrupaciones:
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
        