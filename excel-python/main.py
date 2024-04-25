from Agrupacion import Agrupacion
from MedicionesAgrupacion import MedicionesAgrupacion
from Muestra import Muestra
from Frecuencias import Frecuencias

kmRecorridosCon1LDeNafta = [
  12.5, 11.3, 13.25, 9.5, 10.5,
  13.25, 9.75, 9.25, 7.5, 9.5,
  9.25, 7.9, 8.4, 11.25, 8.75,
  14, 8.6, 13.1, 12.75, 12.5,
  10.5, 12.5, 10.5, 9.25, 11.25,
  13, 9.25, 9.5, 10.9, 11.5,
  9.75, 13, 8.75, 13.25, 9.25,
  7.8, 12.75, 10.25, 12.75, 7.8,
  8.75, 11.75, 11.5, 11.5, 9.4
]
agrupacion = Agrupacion(kmRecorridosCon1LDeNafta, 7, False)
frecuencias = Frecuencias(agrupacion, kmRecorridosCon1LDeNafta)
mediciones = MedicionesAgrupacion(agrupacion, frecuencias, kmRecorridosCon1LDeNafta)
muestra = Muestra(kmRecorridosCon1LDeNafta)
for datos in (muestra, mediciones):
    print(f'Media: {datos.media()}, Mediana: {datos.mediana()}, Moda: {datos.moda()}')
    print(f'Cuartiles: {datos.calcular_cuartiles()}')
    print(f'Percentil: {datos.calcular_percentil(13)}')
    print(f'Varianza: {datos.varianza()}')
