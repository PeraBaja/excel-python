def media (datos: list):
    return round(sum(datos) / len(datos), 2)
def mediana (datos):
    posicionMedio = (len(datos) + 1) / 2
    if type(posicionMedio) == int:
        return posicionMedio
    
    posicion1, posicion2 = (posicionMedio.__floor__(), posicionMedio.__ceil__())
    return (datos[posicion2] - datos[posicion1]) / 2 
def moda (datos):
    return max(datos)