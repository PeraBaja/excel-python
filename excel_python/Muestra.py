from .IMedible import IMedible


class Muestra(IMedible):
    def __init__(self, datos: tuple):
        """_Clase que permite hacer mediciones estadísticas a partir de los datos no agrupados_

        Args:
            datos (tuple)
        """
        self.__datos = datos
        self.__media = self.media()
    def media(self) -> float:
        """_Devuelve el promedio de los datos no agrupados_

        Returns:
            float
        """
        return round(sum(self.__datos) / len(self.__datos), 2)


    def mediana(self) -> float:
        """_Devuelve el promedio de los datos no agrupados_

        Returns:
            float
        """
        self.__datos.sort()
        posicionMedio = (len(self.__datos) + 1) / 2
        if posicionMedio.is_integer():
            return self.__datos[int(posicionMedio)]
        posicion1, posicion2 = (posicionMedio.__floor__(), posicionMedio.__ceil__())
        return (self.__datos[posicion2] + self.__datos[posicion1]) / 2


    def moda(self) -> float:
        """_Devuelve el promedio de los datos no agrupados_

        Returns:
            float
        """
        aparicionMasGrande = 0
        cantidadApariciones = self.__listar_apariciones()
        for dato in cantidadApariciones:
            if cantidadApariciones[dato] > aparicionMasGrande:
                aparicionMasGrande = cantidadApariciones[dato]
                moda = dato
        return moda


    def __listar_apariciones(self) -> dict:
        cantidadApariciones: dict = {}
        
        for dato in self.__datos:
            if not cantidadApariciones.__contains__(dato):
                cantidadApariciones.update({dato: 1})
            else:
                cantidadApariciones[dato] += 1
                
        return cantidadApariciones
            
    def calcular_percentil(self, percentilDeseado: int) -> dict:
        """_Devuelve el percentil a partir de un percentil porcentual (p/100) 
            de los datos no agrupados_

        Args:
            percentilDeseado (_float_): _El porcentaje del percentil_

        Returns:
            _dict_: _Retorna la posicion del percentil como clave y como valor el percentil_
        """
        self.__datos.sort()
        
        posicionPercentil = (percentilDeseado / 100) * len(self.__datos)
            
        if posicionPercentil.is_integer():
            posicionPercentil = int(posicionPercentil)
            percentil = (self.__datos[posicionPercentil - 1] + self.__datos[posicionPercentil]) / 2
        else:
            posicionPercentil = posicionPercentil.__ceil__()
            percentil = self.__datos[posicionPercentil - 1]
        return {posicionPercentil: percentil}
    def varianza(self) -> float:
        """_Devuelve la varianza de los datos no agrupados_

        Returns:
            float
        """
        frecuenciasAbsolutas = self.__listar_apariciones() 
        sumatoria = sum(((dato - self.__media) ** 2) * frecuenciasAbsolutas[dato] for dato in set(self.__datos))
        return sumatoria / len(self.__datos) - 1
        