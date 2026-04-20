# p120-contar-caracteres.py

print('\033[H\033[J')

cadena = input("Ingrese una cadena: ")

frecuencia = {}

for caracter in cadena:
    if caracter not in frecuencia:
        frecuencia[caracter] = 1
    else:
        frecuencia[caracter] += 1

print("\nResultado:")
print(frecuencia)