# p059-pares-descendente.py
# Imprimir los números pares y su suma total en un rango descendente desde 100 hasta un número n que elija el
# usuario.

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---Imprimir los números pares y su suma total en un rango descendente desde 100 hasta un número n---\n')
print('=' * 60)

continuar = 'S'

while continuar.upper() == 'S':
    n = int(input("Introduce un número límite:"))
    
    pares = []
    suma = 0
    i = 100

    while i >= n and i > 0:
        if i % 2 == 0:
            pares.append(str(i))
            suma += i
        i -= 1
    
    if pares:
        print(f"Números pares: {', '.join(pares)}")
        print(f"La suma de los pares es: {suma}")
    else:
        print("No hay números pares en ese rango.")
    
    continuar = input("\n¿Desea continuar (S/N)? ")