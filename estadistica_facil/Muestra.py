

def media(datos: list) -> float:
    """_Devuelve el promedio de los datos no agrupados_

    Returns:
        float
    """
    return round(sum(datos) / len(datos), 2)


def mediana(datos: tuple) -> float:
    """_Devuelve el promedio de los datos no agrupados_

    Returns:
        float
    """
    datos = sorted(datos)
    posicionMedio = (len(datos) + 1) / 2
    if posicionMedio.is_integer():
        return datos[int(posicionMedio)]
    posicion1, posicion2 = (posicionMedio.__floor__(), posicionMedio.__ceil__())
    return (datos[posicion2] + datos[posicion1]) / 2


def moda(datos: tuple, frecuencias_absolutas: tuple) -> float:
    """_Devuelve el promedio de los datos no agrupados_

    Returns:
        float
    """
    frecuencia_maxima = max(frecuencias_absolutas)
    i = frecuencias_absolutas.index(frecuencia_maxima)
    return datos[i]
        
def calcular_percentil(percentilDeseado: int, datos: tuple) -> dict:
    """_Devuelve el percentil a partir de un percentil porcentual (p/100) 
        de los datos no agrupados_

    Args:
        percentilDeseado (_float_): _El porcentaje del percentil_

    Returns:
        _dict_: _Retorna la posicion del percentil como clave y como valor el percentil_
    """
    datos = sorted(datos)
    
    posicionPercentil = (percentilDeseado / 100) * len(datos)
        
    if posicionPercentil.is_integer():
        posicionPercentil = int(posicionPercentil)
        percentil = (datos[posicionPercentil - 1] + datos[posicionPercentil]) / 2
    else:
        posicionPercentil = posicionPercentil.__ceil__()
        percentil = datos[posicionPercentil - 1]
        
    return {posicionPercentil: percentil}

    
def calcular_cuartiles(datos: tuple):
    """_Calcula los percentiles de la posición 25, 50 y 75_

    Args:
        datos (tuple)

    Returns:
        _dict_: _clave: percentil, valor: valor del percentil_
    """
    cuartiles = {}
    for i in range(25, 100, 25):
        percentil = calcular_percentil(i, datos)
        cuartiles.update(percentil)
    return cuartiles

def varianza(datos: tuple, frecuencias_absolutas: tuple) -> float:
    """_Devuelve la varianza de los datos no agrupados_

    Returns:
        float
    """
    media_datos = media(datos)
    sumatoria = 0
    for dato, frecuencia in zip(datos, frecuencias_absolutas):
        sumatoria += ((dato - media_datos) ** 2) * frecuencia
    return sumatoria / (len(datos) - 1)
    