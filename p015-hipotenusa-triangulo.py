# p015-hipotenusa-triangulo.py
# Descripcion de problema:

# Crea un programa que calcule la longitud de la hipotenusa de un triángulo rectángulo. El programa debe solicitar 
# al usuario que ingrese la longitud de los dos lados (catetos) del triángulo. Para el cálculo, utiliza la siguiente
# fórmula:
#            hipotenusa = raizcuadrada( longlado1 * lognlado1 + longlado2 * longlado2 )

import math as mt

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 40)
print ('CALCULANDO LA HIPOTENUSA DE UN TRIANGULO EN PYTHON\n')
print('=' * 40)

# Solicitar los catetos del triangulo en una sola línea separadas por espacio
print('Dame 2 catetos del triangulo separadas por un espacio')
longitud_lado1, longitud_lado2 = input().split()
longitud_lado1, longitud_lado2 = float(longitud_lado1), float(longitud_lado2)


hipotenusa = mt.sqrt(longitud_lado1*longitud_lado1 + longitud_lado2*longitud_lado2)

print(f'La hipotenusa de tu triangulo es: {hipotenusa:.4f}\n')