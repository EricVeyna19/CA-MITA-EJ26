# p038-dia-semana.py
# Descripcion del problema: Escribe un programa que solicite un número entero del 1 al 7 y muestre el día de la semana
# correspondiente, considerando que 1 es domingo y 7 es sábado. Si el número ingresado está fuera de ese rango,
# debe mostrar un mensaje de error.

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---IDENTIFICADOR DEL DIA DE LA SEMANA---\n')
print('=' * 60)

print("Ingresa 1 Numero, del 1 al 7")

# Solicitar los 3 numeros 
numero1 = int(input("Ingresa tu numero: "))

# Ordenarlos numeros
if numero1 == 1:
    print("Salida: Domingo")

elif numero1 == 2:
    print("Salida: Lunes")

elif numero1 == 3:
    print("Salida: Martes")

elif numero1 == 4:
    print("Salida: Miercoles")

elif numero1 == 5:
    print("Salida: Jueves")

elif numero1 == 6:
    print("Salida: Viernes")

elif numero1 == 7:
    print("Salida: Sabado")

else:  
    print("Salida: Numero invalido")

print("Fin del Programa")