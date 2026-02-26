# p060-promedio-suma.py
# Descripcion del problema: Leer números introducidos por el usuario hasta que ingrese un 0. Al finalizar, mostrar el conteo total de números, la
# suma y el promedio de la serie.

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---Leer números introducidos por el usuario hasta que ingrese un 0---\n')
print('=' * 60)

continuar = 'S'

while continuar.upper() == 'S':
    conteo = 0
    suma = 0

    print("Introduce números (0 para terminar):")

    numero = int(input(" "))

    while numero != 0:
        suma += numero
        conteo += 1
        numero = int(input(" "))

    print("-----------------------------------------")

    if conteo > 0:
        promedio = suma / conteo
        print(f"Se introdujeron {conteo} números.")
        print(f"La suma es: {suma}")
        print(f"El promedio es: {promedio}")
    else:
        print("No se introdujo ningún número.")

    continuar = input("\n¿Desea continuar (S/N)?")