# p101-mes-dia-nombre.py
# Leer un número de mes (ej. 4). Guardar los días de cada mes en una lista y los nombres de los meses en otra
# lista. Asumir 28 días para febrero. Imprimir el nombre del mes y la cantidad de días del mes correspondiente (ej. marzo, 30).

print('\033[H\033[J')

# Listas predefinidas con los nombres y días de los meses
nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

try:
    numero_mes = int(input("Introduzca un número de mes (1-12): "))
    
    # Validar que el número de mes esté en el rango correcto
    if 1 <= numero_mes <= 12:
        # Se resta 1 porque los índices de las listas empiezan en 0
        indice = numero_mes - 1 
        
        print("\n--- Resultados ---")
        print(f"Mes: {nombres_meses[indice]}")
        print(f"Días: {dias_meses[indice]}")
    else:
        print("\nNúmero de mes inválido. Debe ser un valor entre 1 y 12.")
except ValueError:
    print("\nEntrada inválida. Por favor, introduzca un número entero.")