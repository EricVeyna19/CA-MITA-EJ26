# p017-convertir-temperatura.py
# Descripcion de problema:
# Desarrolla un programa que convierta una temperatura de grados Celsius a grados Fahrenheit. El programa debe
# solicitar al usuario una temperatura en Celsius y luego mostrar el resultado en Fahrenheit. La fórmula para la
# conversión es: 
# 
#                        farenheit = (celcius × 9/5) + 32

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 40)
print('CONVERSION DE GRADOS CELCIUS A GRADOS FARENHEIT EN PYTHON' )
print('=' * 40)

celcius = float(input('Ingresa la temperatura en grados Celcius: ') )

farenheit = (celcius * 9/5 ) + 32

print(f'{celcius :.4f} grados celcius, equivale a {farenheit :.4f} grados farenheit\n')