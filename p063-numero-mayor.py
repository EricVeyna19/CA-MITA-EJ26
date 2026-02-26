# p063-numero-mayor.py
# Descripcion del problema: Leer una serie de números hasta que el usuario ingrese un 0. Al terminar, el programa deberá mostrar cuál fue el
# número más grande de todos los introducidos.

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---Leer una serie de números hasta que el usuario ingrese un 0. Al terminar, el programa deberá mostrar cuál fue el número más grande de todos los introducidos---\n')
print('=' * 60)

continuar = 'S'

while continuar.upper() == 'S':
    mayor = None
    conteo = 0

    print("Introduce números (0 para terminar):")

    numero = int(input(" "))

    while numero != 0:
        if mayor is None or numero > mayor:
            mayor = numero
        conteo += 1
        numero = int(input(" "))

    print("--------------------")

    if conteo > 0:
        print(f"El número mayor fue: {mayor}")
    else:
        print("No se introdujo ningún número.")

    continuar = input("\n¿Desea continuar (S/N)? ")