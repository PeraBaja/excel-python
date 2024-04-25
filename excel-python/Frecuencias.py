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
        self.__absolutas = self.__calcular_absolutas()
        self.__relativas = self.__calcular_relativas()
        self.__acumuladas = self.__calcular_acumuladas()
    
    absolutas = property(lambda self: self.__absolutas)
    relativas = property(lambda self: self.__relativas)
    acumuladas = property(lambda self: self.__acumuladas)
        

    def __calcular_absolutas(self) :
        absolutas = []
        for intervalo in self.__agrupaciones:
            intervalo: Intervalo
            absolutas.append(
                sum(1 for dato in self.__datos if intervalo.limiteInferior <= dato < intervalo.limiteSuperior)
                )
        return tuple(absolutas)      

    def __calcular_relativas(self):
        relativas = []
        for frecuencia in self.absolutas: 
            relativas.append(
                round(frecuencia / len(self.__datos), 2)
                )
        return tuple(relativas)

    def __calcular_acumuladas(self):
        frecuenciaAcumulada = 0
        acumuladas = []
        for frecuencia in self.absolutas:
            frecuenciaAcumulada += frecuencia
            acumuladas.append(frecuenciaAcumulada)
        return tuple(acumuladas)
        