# p020-numero-suerte.py
# Descripcion de problema:
# Escribe un programa que solicite al usuario su año de nacimiento como un número entero de cuatro dígitos. A partir 
# de este dato, el programa debe:
# 
# Mostrar cada uno de los dígitos individuales del año. Por ejemplo, si el año es 1995, debe mostrar "1", "9","9", "5".
# Calcular y mostrar la suma de los dígitos individuales del año. Siguiendo el ejemplo anterior, la suma sería 1 + 9 + 9 + 5 = 24.

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 40)
print('CALCULO DEL NUMERO DE LA SUERTE')
print('=' * 40)

año = input('Ingresa tu año de nacimiento (4 dígitos):\n')

digito1 = int(año[0])
digito2 = int(año[1])
digito3 = int(año[2])
digito4 = int(año[3])

suma = digito1 + digito2 + digito3 + digito4

print(f'Los dígitos individuales son: "{digito1}", "{digito2}", "{digito3}", "{digito4}"\n')
print(f'La suma de los dígitos es: {digito1} + {digito2} + {digito3} + {digito4} = {suma}\n')
