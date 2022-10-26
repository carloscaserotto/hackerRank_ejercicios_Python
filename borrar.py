def sumar_lista(lista):
    return sum(lista)

def calcular_suma_prom(lista):
    ''' retornar la sumatoria y el promedio de una lista. '''
    suma= sumar_lista(lista) # Llamando a una fx dentro de otra fx
    prom= suma/len(lista) #Calculo el promedio como la suma dividido
    #la cantidad de elementos de la lista
    return suma, prom

numeros = [2,3]
result1,result2 = calcular_suma_prom(numeros)
print("La sumatoria es:", result1, "y el promedio es:", result2)