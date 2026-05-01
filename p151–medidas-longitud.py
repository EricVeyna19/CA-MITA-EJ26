# p151-medidas-longitud.py

print('\033[H\033[J')

def pulgadas_a_cm(pulgadas):
    return pulgadas * 2.54

def metros_a_pies(metros):
    return metros * 3.281

try:
    while True:
        print("\n*** Conversor de Unidades ***")
        print("1. Pulgadas a Centímetros")
        print("2. Metros a Pies")
        print("3. Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            pulgadas = float(input("Introduce pulgadas: "))
            print(f"{pulgadas} pulgadas = {pulgadas_a_cm(pulgadas)} cm")

        elif opcion == 2:
            metros = float(input("Introduce metros: "))
            print(f"{metros} metros = {metros_a_pies(metros)} pies")

        elif opcion == 3:
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

except ValueError:
    print("\nError: Entrada inválida.")