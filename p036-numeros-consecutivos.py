# p036-numeros-consecutivos.py
# Descripcion del problema: Escribe un programa que reciba tres números enteros y determine si son consecutivos. Si lo son,
# muestra un mensaje de confirmación; de lo contrario, informa que no lo son.

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---CLASIFICADOR DE NUMEROS CONSECUTIVOS---\n')
print('=' * 60)

print("Ingresa 3 Numeros, cada uno  con un enter")

# Solicitar los 3 numeros 
numero1 = int(input("Primer  número: "))
numero2 = int(input("Segundo número: "))
numero3 = int(input("Tercer  número: "))


# Ordenarlos numeros
if numero1 < numero2 and numero1 < numero3:
    numero_bajo = numero1
    if numero2 < numero3:
        numero_medio =  numero2
        numero_alto  =  numero3
    else:
        numero_medio = numero3
        numero_alto  = numero2

elif numero2 < numero1 and numero2 < numero3:
    numero_bajo = numero2
    if numero1 < numero3:
        numero_medio = numero1 
        numero_alto  = numero3
    else:
        numero_medio = numero3
        numero_alto  = numero1
else:
    numero_bajo = numero3
    if numero1 < numero2:
        numero_medio = numero1
        numero_alto  = numero2
    else:
        numero_medio, numero_alto = numero2, numero1

print(f"Entrada: {numero1}, {numero2}, {numero3}")
print(f"Entrada Ordenada: {numero_bajo}, {numero_medio}, {numero_alto}")

# Comprobar si son consecutivos
if numero_medio == numero_bajo + 1 and numero_alto == numero_medio + 1:
    print("Salida: Los numeros son consecutivos.")
else:
    print("Salida: Los numeros no son consecutivos.")

print("Fin del Programa")