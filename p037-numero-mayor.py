# p037-numero-mayor.py
# Descripcion del problema: Escribe un programa que reciba tres números enteros e identifique y muestre cuál de ellos es el mayor.

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---CLASIFICADOR DE NUMERO MAYOR---\n')
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
print(f"Salida : El numero mayor es: {numero_alto}")

print("Fin del Programa")
