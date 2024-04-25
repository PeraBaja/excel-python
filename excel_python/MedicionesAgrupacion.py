from .Agrupacion import Agrupacion
from .Frecuencias import Frecuencias
from .IMedible import IMedible

class MedicionesAgrupacion(IMedible):
    def __init__(self, agrupacion: Agrupacion, frecuencias: Frecuencias, datos: tuple):
        """_Clase que permite hacer mediciones estadísticas a partir de los datos agrupados_

        Args:
            agrupacion (Agrupacion)
            frecuencias (Frecuencias): _Las frecuencias correspondientes a la agrupación_
            datos (tuple): _Los datos correspondientes a la agrupación_
        """
        self.__intervalos = agrupacion.intervalos
        self.__agrupacion = agrupacion
        self.__frecuencias = frecuencias
        self.__datos = datos
    def media(self) -> float:
        """_Devuelve el promedio de los datos agrupados_

        Returns:
            float
        """
        resultado = [intervalo.marcaClase * Fi for intervalo, Fi in zip(self.__intervalos, self.__frecuencias.absolutas)]
        return round(sum(resultado) / len(self.__datos), 2)

    def mediana(self) -> float:
        """_Devuelve la mediana de los datos agrupados_

        Returns:
            float
        """
        return self.calcular_percentil(50)[50]
    
    def moda(self) -> float:
        """_Devuelve la moda de los datos agrupados_

        Returns:
            float
        """
        Mo = 0
        fi = 0
        fiAnterior = 0
        fiPosterior = 0
        Li = 0
        for i in range(len(self.__frecuencias.absolutas)):
            if self.__frecuencias.absolutas[i] > Mo:
                Mo = self.__frecuencias.absolutas[i]
                fi = self.__frecuencias.absolutas[i]
                Li = self.__intervalos[i].limiteInferior
                try:
                    fiAnterior = self.__frecuencias.absolutas[i - 1]
                except IndexError:
                    fiAnterior = 0
                try:
                    fiPosterior = self.__frecuencias.absolutas[i + 1]
                except IndexError:
                    fiPosterior = 0
        return round(Li + ((Mo - fiAnterior) / (fi - fiAnterior + fi - fiPosterior))* self.__agrupacion.anchoClase, 2)
        pass
    def calcular_percentil(self, percentilDeseado: float):
        """_Devuelve el percentil a partir de un percentil porcentual (p/100) 
            de los datos agrupados_

        Args:
            percentilDeseado (_float_): _El porcentaje del percentil_

        Returns:
            _dict_: _Retorna el percentil porcentual como clave y como valor el percentil_
        """
        Me = sum(self.__frecuencias.absolutas) * (percentilDeseado / 100)
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
                Li = self.__intervalos[i].limiteInferior
                break #Si encontramos el inmediato mayor a n/2 entonces dejamos de buscar
        pecentil = round(Li + ((Me - FiAnterior) / fi)* self.__agrupacion.anchoClase, 2)    
        return {percentilDeseado: pecentil} 
    def varianza(self) -> float:
        """_Devuelve la varianza de los datos agrupados_

        Returns:
            float
        """
        sumatoria = 0
        cantidadIntervalos = len(self.__intervalos)
        for i in range(cantidadIntervalos):
            sumatoria += (pow(self.__intervalos[i].marcaClase - self.media(), 2)) * self.__frecuencias.absolutas[i]
        return sumatoria / len(self.__datos) - 1
        