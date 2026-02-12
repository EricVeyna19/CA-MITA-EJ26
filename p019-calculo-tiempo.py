# p019-calculo-tiempo.py
# Descripcion de problema:
# Diseña un programa que tome una cantidad de horas como un número entero. El programa debe calcular y mostrar 
# el equivalente de ese tiempo en:
# 
# Días (considerando que 1 día tiene 24 horas)
# Minutos (considerando que 1 hora tiene 60 minutos)
# Segundos (considerando que 1 minuto tiene 60 segundos)


print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 40)
print('CALCULO DE TIEMPO')
print('=' * 40)

horas= int(input('Ingresa el numero de horas que deseas calcular:') )

dias = horas/24
min  = horas*60
seg  = horas*3600


print(f'Tu numero equivale a: {dias:.2f} dias\n')
print(f'Tu numero equivale a: {min:.2f} minutos\n')
print(f'Tu numero equivale a: {seg:.2f} segundos\n')