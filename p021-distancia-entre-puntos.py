# p021-distancia-entre-puntos.py
# Descripcion de problema:
# Crea un programa que calcule la distancia entre dos puntos en un plano cartesiano. El programa debe pedir al usuario
# que ingrese las coordenadas (x,y) del punto A y las coordenadas (x,y) del punto B. Utiliza la siguiente fórmula para
# calcular la distancia:
# 
# d = √((ax-bx)²+(ay-by)²) 

import math as mt

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 40)
print('CALCULO DE LA DISTANCIA ENTRE 2 PUNTOS')
print('=' * 40)


# Solicitar las coordenadas del primer punto
print('Ingresa las coordenadas del primer punto sepadas por un espacio(x1,y1):\n')
x1, y1 = input().split()
x1, y1 = int(x1), int(y1)


# Solicitar las coordenadas del segundo punto
print('Ingresa las coordenadas del segundo punto sepadas por un espacio(x2,y2):\n')
x2, y2 = input().split()
x2, y2 = int(x2), int(y2)

distancia = mt.sqrt(mt.pow((x1-x2),2) + mt.pow((y1-y2),2))

print(f'La distancia entre los puntos es:{distancia:.2f}\n')
