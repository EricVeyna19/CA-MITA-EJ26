# p016-tercer-angulo.py
# Descripcion de problema:

# Escribe un programa que determine el tercer ángulo de un triángulo. El programa debe pedir al usuario que ingrese
# las medidas de dos ángulos del triángulo. Utiliza la siguiente fórmula para encontrar el ángulo faltante:
#
#                       angulo3 = 180 – (angulo1 + angulo2)

import math as mt

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 40)
print ('CALCULA EL 3ER ANGULO DE UN TRIANGULO EN PYTHON\n')
print('=' * 40)

# Solicitar los catetos del triangulo en una sola línea separadas por espacio
print('Ingresa los 2 angulos del triangulo separadas por un espacio')
angulo1, angulo2 = input().split()
angulo1, angulo2 = float(angulo1), float(angulo2)


angulo3 = 180 - (angulo1 + angulo2)

print(f'El 3er angulo de tu triangulo es: {angulo3:.4f}\n')