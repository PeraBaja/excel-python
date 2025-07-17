from abc import abstractmethod, ABC
class IMedible(ABC):
    @abstractmethod
    def media(self) -> float:
        pass

    @abstractmethod
    def mediana(self) -> float:
        pass
    
    @abstractmethod
    def moda(self) -> float:
        pass
    
    @abstractmethod
    def calcular_percentil(self, percentilDeseado) -> dict:
        pass
    
    def calcular_cuartiles(self):
        cuartiles = {}
        for i in range(25, 100, 25):
            percentil = self.calcular_percentil(i)
            cuartiles.update(percentil)
        return cuartiles
    
    @abstractmethod
    def varianza(self) -> float:
        pass