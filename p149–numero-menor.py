# p149-numero-menor.py
# Solicitar 3 números y devolver el menor

print('\033[H\033[J')

def numero_menor(a, b, c):
    return min(a, b, c)

try:
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))
    n3 = int(input("Introduce el tercer número: "))

    menor = numero_menor(n1, n2, n3)

    print("\n--- Resultado ---")
    print(f"El número menor es: {menor}")

except ValueError:
    print("\nError: Ingresa números enteros válidos.")