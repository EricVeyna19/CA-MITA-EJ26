# p099-p099-procesar-notas.py
# Leer un número indeterminado de notas (calificaciones) entre 0 y 100, deteniéndose cuando el usuario introduzc
# un 0. Validar que todas las notas introducidas estén dentro del rango [0,100]. Calcular e imprimir:

print('\033[H\033[J')
print("--- Procesamiento de notas ---\n")

notas = []

while True:
    try:
        entrada = float(input("Introduzca nota (0 para detener): "))
        

        if entrada.is_integer():
            entrada = int(entrada)
            
        if entrada == 0:
            break
        elif 0 < entrada <= 100:
            notas.append(entrada)
        else:
            print("<- Entrada inválida, debe ser 0-100")
    except ValueError:
        print("Por favor, introduzca un número.")

if notas:
    suma = sum(notas)
    promedio = suma / len(notas)
    menores_promedio = [n for n in notas if n < promedio]

    print("\n--- Resultados ---")
    print(f"Total de notas introducidas: {len(notas)}")
    print(f"Lista de notas: {notas}")
    print(f"Suma de notas: {suma}")
    print(f"Promedio de notas: {promedio}")
    print(f"Nota máxima: {max(notas)}")
    print(f"Nota mínima: {min(notas)}")
    print(f"Notas menores al promedio ({promedio}): {len(menores_promedio)}")
    print(f"Lista de notas menores al promedio: {menores_promedio}")
else:
    print("No se introdujeron notas para procesar.")