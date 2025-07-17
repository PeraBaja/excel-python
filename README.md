# Excel en Python

_Una libreria para hacer mediciones estadísticas basicas de datos_

## Instalación
_Instalar la librería en tu proyecto_
```
pip install estadistica-facil
```

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_clona el proyecto_

```
git clone https://github.com/PeraBaja/excel-python.git
```
_instala numpy_

```
pip install numpy
```

## Ejemplos
```python
import estadistica_facil as e

datos = (2, 2, 3, 4, 5, 6, 7)
agrupación = e.Agrupacion(datos, cantidadDeIntervalos=4, redondearAbajo=False)
frecuencias = e.Frecuencias(agrupación, datos)
mediciones_agrupación = e.MedicionesAgrupacion(agrupación, frecuencias, datos)
media = mediciones_agrupación.media()
mediana = mediciones_agrupación.mediana()
moda = mediciones_agrupación.moda()

print(media, mediana, moda)  # Ouput: 4.71, 4.5, 3

muestra = e.Muestra(datos)
moda = muestra.media()
mediana = muestra.mediana()
moda = muestra.moda()

print(media, mediana, moda)  # Ouput: 4.71, 4.5, 3
```
