# p006-conversor-temperatura.py
# Convertir temperatura de grados Celsius a Farenheit

print('Conviriteindo grados Celcius a graos Farenheit: \n')

celcius = float(input('Ingresa la temperatura en grados Celcius: ') )

farenheit = (celcius * 9 / 5 ) + 32

print(f'{celcius :.2f} grados celcius, equivale a {farenheit :.2f} grados farenheit')