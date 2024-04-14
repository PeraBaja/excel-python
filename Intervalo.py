class Intervalo:
    def __init__(self, limiteInferior, LimiteSuperior, datos) :
        self.__limiteInferior = limiteInferior
        self.__limiteSuperior = LimiteSuperior
        self.__datos = datos

    def frecuenciaAbsoluta(self) :
        frecuenciaAbsoluta = sum(1 for dato in self.__datos if self.__limiteInferior <= dato < self.__limiteSuperior)
        return frecuenciaAbsoluta

    def frecuenciaRelativa(self):
        return round(self.frecuenciaAbsoluta() / len(self.__datos), 2)

    def __str__(self):
        return f'{self.__limiteInferior}-{self.__LimiteSuperior}'
    @property
    def _limeteInferior(self):
      return self.__limiteInferior
    
    @property
    def limiteSuperior(self):
      return self.__limiteSuperior
  

    
