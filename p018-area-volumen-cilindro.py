# p018-area-volumen-cilindro.py
# Descripcion de problema:
# Crea un programa que calcule el área y volumen de un cilindro. Pide al usuario que ingrese el radio y la altura del
# cilindro. Las fórmulas para el cálculo de área y de volumen son:
# 
# Area = PI * radio * (radio + alto)
# Volumen = PI * (Radio * Radio) * Altura

import math as mt

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 40)
print('CALCULO DEL AREA Y EL VOLUMEN DE UN CILINDRO')
print('=' * 40)

radio = float(input('Ingresa el radio de la base tu cilindro: ') )
altura = float(input('Ingresa la altura de tu cilindro: ') )

Area    = 2* mt.pi * radio * (radio + altura)
Volumen = mt.pi * (radio * radio) * altura



print(f'El area es: {Area:.4f} y el volumen es: {Volumen :.4f}\n')