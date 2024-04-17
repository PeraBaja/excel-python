from dataclasses import dataclass, field

@dataclass(frozen=True, slots=True)
class Intervalo:
    limiteInferior: float
    limiteSuperior: float
    marcaClase = field(init=False, default=(limiteSuperior + limiteInferior) / 2)

    
