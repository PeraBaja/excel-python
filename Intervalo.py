class Intervalo:
    def __init__(self, limeteInferior, LimiteSuperior, datos) :
        self.limeteInferior = limeteInferior
        self.LimiteSuperior = LimiteSuperior
        self.__datos = datos

    def frecuenciaAbsoluta(self) :
        frecuenciaAbsoluta = sum(1 for dato in self.__datos if self.limeteInferior <= dato < self.LimiteSuperior)
        return frecuenciaAbsoluta

    def frecuenciaRelativa(self):
        return round(self.frecuenciaAbsoluta() / len(self.__datos), 2)

    def __str__(self):
        return f'{self.limeteInferior}-{self.LimiteSuperior}'
