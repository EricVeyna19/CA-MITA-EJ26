# p064-verificar-palindromo.py
# Solicitar al usuario que ingrese un número entero y determinar si es un palíndromo. Un número es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda (ej. 121, 3443).

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---Verificacion de numeros palindromos---\n')
print('=' * 60)

continuar = 'S'

while continuar.upper() == 'S':
    numero = input("Introduce un número: ")

    invertido = numero[::-1]

    if numero == invertido:
        print(f"El número {numero} es un palíndromo.")
    else:
        print(f"El número {numero} no es un palíndromo.")

    continuar = input("\n¿Desea continuar (S/N)? ")