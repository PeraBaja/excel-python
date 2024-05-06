"""_Permite realizar operaciones estadisticas de manera sencilla_"""
from estadistica_facil.agrupacion import calcular_anchoClase, agrupar
from estadistica_facil.frecuencias import frecuencias_absolutas, frecuencias_acumuladas, frecuencias_relativas
from estadistica_facil.Intervalo import Intervalo
import estadistica_facil.medicionesAgrupacion
import estadistica_facil.muestra

__version__ = "1.0.17"
print("Clases importadas correctamente")
__all__ = ['calcular_anchoClase', 'agrupar', 'frecuencias', 'Intervalo', 'medicionesAgrupacion', 'muestra']