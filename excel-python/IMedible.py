from abc import abstractmethod, ABC
class IMedible(ABC):
    @abstractmethod
    def media():
        pass

    @abstractmethod
    def mediana():
        pass
    
    @abstractmethod
    def moda():
        pass
    
    @abstractmethod
    def calcular_percentil(self, percentilDeseado):
        pass
    
    def calcular_cuartiles(self):
        cuartiles = {}
        for i in range(25, 100, 25):
            percentil = self.calcular_percentil(i)
            cuartiles.update(percentil)
        return cuartiles
    
    @abstractmethod
    def varianza():
        pass