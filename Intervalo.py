class Intervalo:
    def __init__(self, limiteInferior, limiteSuperior) :
        self.__limiteInferior = limiteInferior
        self.__limiteSuperior = limiteSuperior

    def __str__(self):
        return f'{self.__limiteInferior}-{self.__limiteSuperior}'
    @property
    def limiteInferior(self):
      return self.__limiteInferior
    
    @property
    def limiteSuperior(self):
      return self.__limiteSuperior
  

    
