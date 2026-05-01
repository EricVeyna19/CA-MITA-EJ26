# p152-suma-pares-impares.py
# Sumar números pares o impares dentro de un rango usando una función.

print('\033[H\033[J')

def suma_rango(inicio, fin, tipo):
    numeros = []

    for n in range(inicio, fin + 1):
        if tipo == 'P' and n % 2 == 0:
            numeros.append(n)
        elif tipo == 'I' and n % 2 != 0:
            numeros.append(n)

    suma = sum(numeros)
    return suma, numeros

try:
    print("*** Suma en Rango ***")

    inicio = int(input("Introduce el número inicial: "))
    fin = int(input("Introduce el número final: "))
    tipo = input("¿Qué deseas sumar? (P)ares o (I)mpares: ").upper()

    if tipo == 'P' or tipo == 'I':
        resultado, numeros = suma_rango(inicio, fin, tipo)

        if tipo == 'P':
            texto = "pares"
        else:
            texto = "impares"

        print(f"\nLa suma de los números {texto} entre {inicio} y {fin} es: {resultado}")

        calculo = " + ".join(str(n) for n in numeros)
        print(f"(Cálculo: {calculo} = {resultado})")

    else:
        print("\nError: Debes escribir P para pares o I para impares.")

except ValueError:
    print("\nError: Ingresa solamente números enteros válidos.")