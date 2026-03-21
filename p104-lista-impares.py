# p104-lista-impares.py
# Leer un entero n. Llenar una lista con los primeros n números impares.
# Calcular e imprimir: La suma y el promedio de los números. Los números que son divisibles entre 3 y su suma.
# Pedir un elemento a buscar en la lista original e indicar si está y en qué posición (índice).

print('\033[H\033[J')

try:
    n = int(input("Introduzca la cantidad de números impares (n): "))
    
    # Generar la lista con los primeros 'n' números impares
    # Usamos n * 2 en el rango con pasos de 2 para obtener exactamente 'n' elementos
    impares = [x for x in range(1, n * 2, 2)]
    
    print("\n--- Generación de Lista ---")
    print(f"Lista de los primeros {n} números impares: {impares}")
    
    if impares:
        # Cálculos de suma y promedio
        suma = sum(impares)
        promedio = suma / len(impares)
        
        print("\n--- Cálculos ---")
        print(f"Suma de los números: {suma}")
        print(f"Promedio de los números: {promedio}")
        
        # Divisibles entre 3
        divisibles_3 = [x for x in impares if x % 3 == 0]
        suma_div_3 = sum(divisibles_3)
        
        print("\n--- Divisibles entre 3 ---")
        print(f"Números divisibles entre 3: {divisibles_3}")
        print(f"Suma de los números divisibles entre 3: {suma_div_3}")
        
        # Búsqueda de elemento
        print("\n--- Búsqueda ---")
        buscar = int(input("Introduzca elemento a buscar: "))
        
        if buscar in impares:
            indice = impares.index(buscar)
            print(f"Result: El elemento {buscar} está en la lista en la posición (índice) {indice}.")
        else:
            print(f"Result: El elemento {buscar} no está en la lista.")
    else:
        print("\nNo se generaron números para la lista (n debe ser mayor a 0).")

except ValueError:
    print("\nError: Por favor introduzca un número entero válido.")