def media(datos: list):
    return round(sum(datos) / len(datos), 2)


def mediana(datos: list):
    datos.sort()
    posicionMedio = (len(datos) + 1) / 2
    if posicionMedio.is_integer():
        return datos[int(posicionMedio)]
    posicion1, posicion2 = (posicionMedio.__floor__(), posicionMedio.__ceil__())
    return (datos[posicion2] + datos[posicion1]) / 2


def moda(datos: list):
    aparicionMasGrande = 0
    cantidadApariciones = __listar_apariciones(datos)
    for dato in cantidadApariciones:
        if cantidadApariciones[dato] > aparicionMasGrande:
            aparicionMasGrande = cantidadApariciones[dato]
            moda = dato
    return moda


def __listar_apariciones(datos: list) -> dict:
    cantidadApariciones: dict = {}
    
    for dato in datos:
        if not cantidadApariciones.__contains__(dato):
            cantidadApariciones.update({dato: 1})
        else:
            cantidadApariciones[dato] += 1
            
    return cantidadApariciones


def calcular_cuartiles(datos: list) -> dict:
    cuartiles = {}
    cuartil = {}
    for p in range(25, 100, 25):
        cuartil = calcular_percentil(datos, p)
        cuartiles.update(cuartil)
    return cuartiles
        
def calcular_percentil(datos: list, percentilDeseado: int):
    datos.sort()
    
    posicionPercentil = (percentilDeseado / 100) * len(datos)
        
    if posicionPercentil.is_integer():
        posicionPercentil = int(posicionPercentil)
        percentil = (datos[posicionPercentil - 1] + datos[posicionPercentil]) / 2
    else:
        posicionPercentil = posicionPercentil.__ceil__()
        percentil = datos[posicionPercentil - 1]
    return {posicionPercentil: percentil}
