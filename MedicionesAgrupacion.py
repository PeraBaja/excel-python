from Agrupacion import Agrupacion
from Frecuencias import Frecuencias


class MedicionesAgrupacion:
    def __init__(self, agrupacion: Agrupacion, frecuencias: Frecuencias):
        self.__agrupacion = agrupacion
        self.__frecuencias = frecuencias
    def media(self):
        resultado = [intervalo.marcaClase * Fi for intervalo, Fi in zip(self.__agrupacion, self.__frecuencias.absolutas)]
        return round(sum(resultado) / len(self.__datos), 2)

    def mediana(self):
        Me = sum(self.__frecuencias.Absolutas) / 2
        FiAnterior = 0
        fi = 0
        Li = 0
        for i in range(len(self.__frecuencias.acumuladas)):
            if self.__frecuencias.acumuladas[i] > Me:
                try:
                    FiAnterior = self.__frecuencias.acumuladas[i - 1]
                except IndexError:
                    FiAnterior = 0
                fi = self.__frecuencias.absolutas[i]
                Li = self.__agrupacion[i].limiteInferior
                break
        return round(Li + ((Me - FiAnterior) / fi)* self.anchoClase, 2)
    
    def moda(self):
        Mo = 0
        fi = 0
        fiAnterior = 0
        fiPosterior = 0
        Li = 0
        for i in range(len(self.__frecuencias.absolutas)):
            if self.__frecuencias.absolutas[i] > Mo:
                Mo = self.__frecuencias.absolutas[i]
                fi = self.__frecuencias.absolutas[i]
                Li = self.__agrupacion[i].limiteInferior
                try:
                    fiAnterior = self.__frecuencias.absolutas[i - 1]
                except IndexError:
                    fiAnterior = 0
                try:
                    fiPosterior = self.__frecuencias.absolutas[i + 1]
                except IndexError:
                    fiPosterior = 0
        return round(Li + ((Mo - fiAnterior) / (fi - fiAnterior + fi - fiPosterior))* self.anchoClase, 2)
    