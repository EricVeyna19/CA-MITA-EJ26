# p085-rombo-caracter.py
# Solicitar al usuario un número entero impar n que representará la altura y el ancho 
# máximo de un rombo. El programa deberá dibujar el rombo utilizando el carácter 
# que el usuario elija.

print("\033[H\033[J")

n = 0
while n % 2 == 0 or n <= 0:
    n = int(input("Dame un número impar para la altura: "))

caracter = input("¿Qué carácter quieres usar? ")

mitad = n // 2

# Dibuja la parte superior y el centro
for i in range(mitad + 1):
    espacios = " " * (mitad - i)
    caracteres = caracter * (2 * i + 1)
    print(espacios + caracteres)

# Dibuja la parte inferior
for i in range(mitad - 1, -1, -1):
    espacios = " " * (mitad - i)
    caracteres = caracter * (2 * i + 1)
    print(espacios + caracteres)