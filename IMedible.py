from abc import abstractmethod, ABCMeta
class IMedible(ABCMeta):
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
    def calcular_percentil():
        pass
    
    @abstractmethod
    def calcular_cuartiles():
        pass
    
    @abstractmethod
    def varianza():
        pass