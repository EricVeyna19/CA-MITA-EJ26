# p100-listas-multiplica.py
# Leer dos listas, cada una con 5 elementos numéricos. Crear una tercera lista multiplicando los elementos de las
# dos listas correspondientes. Imprimir las tres listas.

print('\033[H\033[J')
print("--- Multiplicación de Listas ---\n")

# Se utiliza .split() para separar los números introducidos con espacios en una sola línea
lista_a = [int(x) for x in input("Introduzca 5 números separados por un espacio para la Lista A: ").split()]
lista_b = [int(x) for x in input("Introduzca 5 números separados por un espacio para la Lista B: ").split()]

# Se crea la tercera lista multiplicando los elementos en la misma posición (índice)
lista_c = [lista_a[i] * lista_b[i] for i in range(5)]

print("\n--- Resultados ---")
print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")
print(f"Lista C (A * B): {lista_c}")