# p084-cuadro-hueco-caracter.py
# El programa debe solicitar al usuario que ingrese el tamaño del lado de un cuadrado 
# y el carácter con el que se dibujará. Luego, deberá imprimir en la consola un 
# "cuadrado hueco", donde el carácter solo se utilice para dibujar el contorno del mismo.

print("\033[H\033[J")

tamaño = int(input("¿De qué tamaño será el lado del cuadrado? "))
caracter = input("¿Qué carácter quieres usar? ")

for i in range(tamaño):
    for j in range(tamaño):
        # Condición para imprimir el carácter en los bordes
        if i == 0 or i == tamaño - 1 or j == 0 or j == tamaño - 1:
            print(caracter, end=" ")
        else:
            # Imprime espacios en el interior del cuadrado
            print(" ", end=" ")
    # Salto de línea al terminar cada fila
    print()