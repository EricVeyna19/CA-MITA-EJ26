# p155-estadisticas-basicas.py
# Calcular estadísticas básicas poblacionales para una lista de números.

print('\033[H\033[J')

import math

def leer_lista():
    datos = input("Dame números separados por espacio: ")
    lista = [int(x) for x in datos.split()]
    return lista

def numero_mayor(lista):
    return max(lista)

def numero_menor(lista):
    return min(lista)

def media(lista):
    return sum(lista) / len(lista)

def varianza_poblacional(lista):
    promedio = media(lista)
    suma = 0

    for x in lista:
        suma += (x - promedio) ** 2

    return suma / len(lista)

def desviacion_estandar_poblacional(lista):
    return math.sqrt(varianza_poblacional(lista))

try:
    numeros = leer_lista()

    if len(numeros) > 0:
        print(f"\nLista de números: {numeros}")

        print("\nEstadísticas:")
        print(f"Media                 : {media(numeros):.3f}")
        print(f"Mayor                 : {numero_mayor(numeros)}")
        print(f"Menor                 : {numero_menor(numeros)}")
        print(f"Varianza              : {varianza_poblacional(numeros):.3f}")
        print(f"Desviación estándar   : {desviacion_estandar_poblacional(numeros):.3f}")

    else:
        print("\nError: La lista no puede estar vacía.")

except ValueError:
    print("\nError: Ingresa solamente números enteros válidos.")