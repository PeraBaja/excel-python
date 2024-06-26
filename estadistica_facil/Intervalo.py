from dataclasses import dataclass, field

@dataclass(frozen=True, slots=True)
class Intervalo:
    """_Crea un intervalo con un limite inferior y un limite superior_
    Args:
        limiteInferior (float)
        limiteSuperior (float)
    """
    limiteInferior: float
    limiteSuperior: float
    marcaClase: float = field(init=False)
    
    def __post_init__(self):
          object.__setattr__(self, 'marcaClase', (self.limiteInferior + self.limiteSuperior) / 2)
    
    def __repr__(self) -> str:
         return f'{self.limiteInferior}-{self.limiteSuperior}'