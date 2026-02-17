# p035-tipo-triangulo.py
# Objetivo: Clasificar un triángulo según la longitud de sus tres lados.
print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---CLASIFICADOR DE TRIÁNGULOS---\n')
print('=' * 60)

print("Ingresa la longitud de los tres lados de un triángulo.")

# Solicitar la longitud de los lados
l1 = float(input("Ingresa la longitud del primer lado: "))
l2 = float(input("Ingresa la longitud del segundo lado: "))
l3 = float(input("Ingresa la longitud del tercer lado: "))

if l1 == 12 == 13 :
    print('Es un triángulo EQUILÁTERO (todos los lados son iguales)')
elif l1 == 12 or l1 == 13 or 12 == 13:
    print('Es un triángulo ISÓSCELES (al menos dos lados son iguales)')
else:
    print('Es un triángulo ESCALENO (ningún lado es igual)')

print('\nAdios, gracias por utilizar este programa')