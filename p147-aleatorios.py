# p147-aleatorios.py
# Genera dos listas de números aleatorios y crea una tercera lista que sea la suma de las dos primeras.

print('\033[H\033[J')


import random
from typing import List

def generar_numeros_aleatorios(n: int, minimo: int, maximo: int) -> List[int]:
    numeros_aleatorios = []
    for _ in range(n):
        numero = random.randint(minimo, maximo)
        numeros_aleatorios.append(numero)
    return numeros_aleatorios

def sumar_listas(lista1: List[int], lista2: List[int]) -> List[int]:
    suma = []
    for a, b in zip(lista1, lista2):
        suma.append(a + b)
    return suma

# Ejemplo de uso
lista1 = generar_numeros_aleatorios(5, 1, 10)
lista2 = generar_numeros_aleatorios(5, 50, 100)
lista3 = sumar_listas(lista1, lista2)

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Suma de listas: {lista3}")