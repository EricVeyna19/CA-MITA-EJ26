# p022-resistencia-equivalente-paralelo.py
# Descripcion de problema:
#Crea un programa que calcule la resistencia total o equivalente de un circuito con cuatro resistencias en paralelo.
# El programa debe solicitar al usuario que ingrese el valor de cada una de las cuatro resistencias (R1, R2, R3 y R4).
# Luego, debe calcular la resistencia total usando la siguiente fórmula:
# 
# rt = 1/( (1/r1) + (1/r2) + (1/r3) + (1/r4) )

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 40)
print('CALCULO DE LA RESISTENCIA EQUIVALENTE DE UN CIRCUITO PARALELO')
print('=' * 40)


# Solicitar las resistencias del circuito
r1= int(input('Ingresa R1 del circuito:\n'))
r2= int(input('Ingresa R2 del circuito:\n'))
r3= int(input('Ingresa R3 del circuito:\n'))
r4= int(input('Ingresa R4 del circuito:\n'))

rt = 1/( (1/r1) + (1/r2) + (1/r3) + (1/r4) )

print(f'La resistencia equivalente es:{rt:.3f}\n')