# p153-suma-digitos.py

print('\033[H\033[J')

def leer_lista():
    datos = input("Dame números separados por espacio: ")
    return [int(x) for x in datos.split()]

def suma_digitos(num):
    return sum(int(d) for d in str(abs(num)))

def procesar_lista(lista):
    return [suma_digitos(x) for x in lista]

try:
    lista = leer_lista()

    nueva = procesar_lista(lista)

    print("\n--- Resultados ---")
    print(f"Lista original: {lista}")
    print(f"Suma de dígitos: {nueva}")

except ValueError:
    print("\nError: Entrada inválida.")