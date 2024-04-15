def media (datos: list):
    return round(sum(datos) / len(datos), 2)

def mediana (datos):
    posicionMedio = (len(datos) + 1) / 2
    if posicionMedio.is_integer():
        return datos[int(posicionMedio)]    
    posicion1, posicion2 = (posicionMedio.__floor__(), posicionMedio.__ceil__())
    return (datos[posicion2] + datos[posicion1]) / 2 

def moda (datos):

    aparicionMasGrande = 0
    cantidadApariciones = __listar_apariciones(datos)
    for dato in cantidadApariciones:
        if cantidadApariciones[dato] > aparicionMasGrande:
            aparicionMasGrande = cantidadApariciones[dato]
            moda = dato
    return moda

def __listar_apariciones(datos) -> dict:
    cantidadApariciones: dict = {}
    for dato in datos:
        if not cantidadApariciones.__contains__(dato):
            cantidadApariciones.update({dato: 1})
        else:
            cantidadApariciones[dato] += 1
    return cantidadApariciones