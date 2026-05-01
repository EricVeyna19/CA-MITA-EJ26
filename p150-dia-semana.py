# p150-dia-semana.py

print('\033[H\033[J')

def dia_semana(num):
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    return dias.get(num, None)

try:
    n = int(input("Introduce un número del 1 al 7: "))

    dia = dia_semana(n)

    print("\n--- Resultado ---")
    if dia:
        print(f"El día es: {dia}")
    else:
        print("Error: El número debe estar entre 1 y 7.")

except ValueError:
    print("\nError: Ingresa un número entero válido.")