from agrupacion import Agrupaciones
from datos_no_agrupados import media, mediana, moda 
from Intervalo import Intervalo
kmRecorridosCon1LDeNafta = [
  12.5, 11.3, 13.25, 9.5, 10.5,
  13.25, 9.75, 9.25, 7.5, 9.5,
  9.25, 7.9, 8.4, 11.25, 8.75,
  14, 8.6, 13.1, 12.75, 12.5,
  10.5, 12.5, 10.5, 9.25, 11.25,
  13, 9.25, 9.5, 10.9, 11.5,
  9.75, 13, 8.75, 13.25, 9.25,
  7.8, 12.75, 10.25, 12.75, 7.8,
  8.75, 11.75, 11.5, 11.5, 9.4, 8
]
agrupaciones = Agrupaciones(kmRecorridosCon1LDeNafta, 7, False)
print(agrupaciones, agrupaciones.anchoClase, agrupaciones.frecuenciasAbsolutas, agrupaciones.frecuenciasRelativas)
print(f'Media: {media(kmRecorridosCon1LDeNafta)}, Mediana: {mediana(kmRecorridosCon1LDeNafta)}, Moda: {moda(kmRecorridosCon1LDeNafta)}')