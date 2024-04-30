"""_Permite realizar operaciones estadisticas de manera sencilla_"""
from estadistica_facil.agrupacion import calcular_anchoClase, agrupar
from estadistica_facil.Frecuencias import Frecuencias
from estadistica_facil.Intervalo import Intervalo
from estadistica_facil.MedicionesAgrupacion import MedicionesAgrupacion
from estadistica_facil.Muestra import Muestra
__version__ = "1.0.17"
print("Clases importadas correctamente")
__all__ = ['Agrupacion', 'Frecuencias', 'Intervalo', 'MedicionesAgrupacion', 'Muestra']