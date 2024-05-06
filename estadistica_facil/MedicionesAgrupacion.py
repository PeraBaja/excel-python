from estadistica_facil.frecuencias import frecuencias_acumuladas

def media(intervalos: tuple, datos: tuple, frecuencias_absolutas: tuple) -> float:
    """_Devuelve el promedio de los datos agrupados_

    Returns:
        float
    """
    resultado = [intervalo.marcaClase * Fi for intervalo, Fi in zip(intervalos, frecuencias_absolutas)]
    return round(sum(resultado) / len(datos), 2)

def mediana() -> float:
    """_Devuelve la mediana de los datos agrupados_

    Returns:
        float
    """
    return calcular_percentil(50)[50]

def moda(intervalos: tuple, datos: tuple, frecuencias_absolutas: tuple, ancho_clase) -> float:
    """_Devuelve la moda de los datos agrupados_
    Args:
        intervalos (tuple): _description_
        datos (tuple): _description_
        frecuencias_absolutas (tuple): _description_
        ancho_clase (_int_): _description_

    Returns:
        float: _moda_
    """
    Mo = 0
    fi = 0
    fiAnterior = 0
    fiPosterior = 0
    Li = 0
    for i in range(len(frecuencias_absolutas)):
        if frecuencias_absolutas[i] > Mo:
            Mo = frecuencias_absolutas[i]
            fi = frecuencias_absolutas[i]
            Li = intervalos[i].limiteInferior
            try:
                fiAnterior = frecuencias_absolutas[i - 1]
            except IndexError:
                fiAnterior = 0
            try:
                fiPosterior = frecuencias_absolutas[i + 1]
            except IndexError:
                fiPosterior = 0
    return round(Li + ((Mo - fiAnterior) / (fi - fiAnterior + fi - fiPosterior))* ancho_clase, 2)
    pass
def calcular_percentil(percentilDeseado: float, intervalos: tuple, datos: tuple, frecuencias_absolutas: tuple, ancho_clase: int):
    """_Devuelve el percentil a partir de un percentil porcentual (p/100) 
        de los datos agrupados_

    Args:
        percentilDeseado (_float_): _El porcentaje del percentil_

    Returns:
        _dict_: _Retorna el percentil porcentual como clave y como valor el percentil_
    """
    acumuladas = frecuencias_acumuladas(frecuencias_absolutas)
    Me = sum(frecuencias_absolutas) * (percentilDeseado / 100)
    FiAnterior = 0
    fi = 0
    Li = 0
    for i in range(len(acumuladas)):
        if acumuladas[i] > Me:
            try:
                FiAnterior = acumuladas[i - 1]
            except IndexError:
                FiAnterior = 0
            fi = frecuencias_absolutas[i]
            Li = intervalos[i].limiteInferior
            break #Si encontramos el inmediato mayor a n/percentilDeseado entonces dejamos de buscar
    pecentil = round(Li + ((Me - FiAnterior) / fi)* ancho_clase, 2)    
    return {percentilDeseado: pecentil} 
def varianza(intervalos: tuple, datos: tuple, frecuencias_absolutas: tuple) -> float:
    """_Devuelve la varianza de los datos agrupados_

    Returns:
        float
    """
    X = media(intervalos, datos, frecuencias_absolutas)
    sumatoria = 0
    cantidadIntervalos = len(intervalos)
    for i in range(cantidadIntervalos):
        sumatoria += (pow(intervalos[i].marcaClase - X, 2)) * frecuencias_absolutas[i]
    return sumatoria / len(datos) - 1 ##Error de calculo
    