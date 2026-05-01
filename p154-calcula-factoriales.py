# p154-calcula-factoriales.py

print('\033[H\033[J')

def leer_lista():
    datos = input("Dame números separados por espacio: ")
    return [int(x) for x in datos.split()]

def factorial(n):
    if n < 0:
        return None
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def procesar(lista):
    return [factorial(x) for x in lista]

try:
    lista = leer_lista()
    resultado = procesar(lista)

    print("\n--- Resultados ---")
    print(f"Lista original: {lista}")
    print(f"Factoriales: {resultado}")

except ValueError:
    print("\nError: Entrada inválida.")