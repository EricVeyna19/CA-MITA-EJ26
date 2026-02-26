# p058-impares-ascendente.py
# Descripcion del problema: Imprimir los números pares y su suma total en un rango descendente desde 100 hasta un número n que elija el
# usuario.
print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---Imprimir los números impares y su suma total en un rango ascendente desde 1 hasta un número n---\n')
print('=' * 60)

continuar = 'S'

while continuar.upper() == 'S':
    n = int(input("Introduce un número límite: "))
    
    impares = []
    suma = 0
    i = 1
    
    while i <= n:
        if i % 2 != 0:
            impares.append(str(i))
            suma += i
        i += 1
    
    if impares:
        print(f"Números impares: {', '.join(impares)}")
        print(f"La suma de los impares es: {suma}")
    else:
        print("No hay números impares en ese rango.")
    
    continuar = input("\n¿Desea continuar (S/N)? ")