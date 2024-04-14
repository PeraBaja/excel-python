class Intervalo:
    def __init__(self, limiteInferior, LimiteSuperior, datos) :
        self.__limiteInferior = limiteInferior
        self.__LimiteSuperior = LimiteSuperior
        self.__datos = datos

    def frecuenciaAbsoluta(self) :
        frecuenciaAbsoluta = sum(1 for dato in self.__datos if self.limeteInferior <= dato < self.LimiteSuperior)
        return frecuenciaAbsoluta

    def frecuenciaRelativa(self):
        return round(self.frecuenciaAbsoluta() / len(self.__datos), 2)

    def __str__(self):
        return f'{self.__limiteInferior}-{self.__LimiteSuperior}'
    @property
    def _limeteInferior(self):
      return self.__limiteInferior
    
    @_limeteInferior.setter
    def _limiteInferior(self, new__limiteInferior):
        if type(new__limiteInferior) != float:
            print("Error. Los limites deben ser floats")
            raise TypeError
        self.__LimiteSuperior = new__limiteInferior 
    @property
    def _LimiteSuperior(self):
      return self.__LimiteSuperior
    
    @_LimiteSuperior.setter
    def _LimiteSuperior(self, new__LimiteSuperior):
        if type(new__LimiteSuperior) != float:
            print("Error. Los limites deben ser floats")
            raise TypeError
        self.__LimiteSuperior = new__LimiteSuperior
  

    
