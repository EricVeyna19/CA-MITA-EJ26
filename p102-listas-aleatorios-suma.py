# p102-listas-aleatorios-suma.py
# Generar 2 listas de 10 números aleatorios cada una. Crear una tercera lista donde el elemento sea la suma de
# los correspondientes de las listas A y B, solo si AMBOS elementos son impares; de lo contrario, el elemento de
# la tercera lista será 0. Imprimir las 3 listas.

import random

print('\033[H\033[J')

# Generamos dos listas con 10 números aleatorios (entre 1 y 20 para mantener números pequeños)
lista_a = [random.randint(1, 20) for _ in range(10)]
lista_b = [random.randint(1, 20) for _ in range(10)]

lista_c = []

# Evaluamos cada elemento por su índice
for i in range(10):
    # Verificamos si ambos son impares (el residuo de la división entre 2 es diferente de 0)
    if lista_a[i] % 2 != 0 and lista_b[i] % 2 != 0:
        lista_c.append(lista_a[i] + lista_b[i])
    else:
        lista_c.append(0)

print("--- Listas Generadas ---")
print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")

print("\n--- Resultados (Suma solo si A[i] y B[i] son ambos impares) ---")
print(f"Lista C: {lista_c}")