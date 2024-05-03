from estadistica_facil.agrupacion import calcular_anchoClase, agrupar
from estadistica_facil.Intervalo import Intervalo

        

def frecuencias_absolutas(datos: tuple, intervalos: tuple = None) :
    datos = sorted(datos)
    print(datos)
    absolutas = []
    if not intervalos:
        return __listar_apariciones(datos)
    for intervalo in intervalos:
        intervalo: Intervalo
        if intervalo == intervalos[-1]:  # Si es el último intervalo
            absolutas.append(
                sum(1 for dato in datos if intervalo.limiteInferior <= dato <= intervalo.limiteSuperior)
            )
        else:
            absolutas.append(
                sum(1 for dato in datos if intervalo.limiteInferior <= dato < intervalo.limiteSuperior)
            )
    return tuple(absolutas)      
def __listar_apariciones(datos: tuple) -> tuple:
        cantidadApariciones: dict = {}
        
        for dato in datos:
            if not cantidadApariciones.__contains__(dato):
                cantidadApariciones.update({dato: 1})
            else:
                cantidadApariciones[dato] += 1
                
        return [frecuencia for frecuencia in cantidadApariciones.values()]
    
def frecuencias_relativas(frecuencias_absolutas: tuple):
    relativas = []
    cantDatos = sum(frecuencias_absolutas)
    for frecuencia in frecuencias_absolutas: 
        relativas.append(
            round(frecuencia / cantDatos, 2)
            )
    return tuple(relativas)

def frecuencias_acumuladas(frecuencias_absolutas: tuple):
    frecuencia = 0
    acumuladas = []
    for frecuencia in frecuencias_absolutas:
        frecuencia += frecuencia
        acumuladas.append(frecuencia)
    return tuple(acumuladas)
        