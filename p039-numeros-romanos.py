# p039-numeros-romanos.py
# Descripcion del problema: Escribe un programa que pida al usuario un número entero entre 1 y 10 y muestre su equivalente en 
# números romanos. Si el número está fuera de este rango, debe mostrar un mensaje de error.

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---IDENTIFICADOR DE NUMERO ROMANOS---\n')
print('=' * 60)

print("Ingresa 1 Numero, del 1 al 10")

# Solicitar  el numero
numero1 = int(input("Ingresa tu numero: "))

# Ordenarlos numeros
if numero1 == 1:
    print("Salida: I")

elif numero1 == 2:
    print("Salida: II")

elif numero1 == 3:
    print("Salida: III")

elif numero1 == 4:
    print("Salida: IV")

elif numero1 == 5:
    print("Salida: V")

elif numero1 == 6:
    print("Salida: VI")

elif numero1 == 7:
    print("Salida: VII")

elif numero1 == 8:
    print("Salida: VIII")

elif numero1 == 9:
    print("Salida: IX")

elif numero1 == 10:
    print("Salida: X")

else:  
    print("Salida: Numero invalido")

print("Fin del Programa")