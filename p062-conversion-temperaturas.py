# p062-conversion-temperaturas.py
# Descripcion del problema: El usuario debe introducir una temperatura inicial y una final en grados Celsius. El programa mostrará la conversión
# a grados Fahrenheit para cada grado en ese rango, incrementando de uno en uno.

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---El usuario debe introducir una temperatura inicial y una final en grados Celsius.---\n')
print('=' * 60)

continuar = 'S'

while continuar.upper() == 'S':
    inicial = int(input("Introduce la temperatura inicial en °C: "))
    final = int(input("Introduce la temperatura final en °C: "))

    print("--------------------")

    temp = inicial
    while temp <= final:
        fahrenheit = (temp * 9/5) + 32
        print(f"{temp}°C = {fahrenheit}°F")
        temp += 1

    continuar = input("\n¿Desea continuar (S/N)? ")