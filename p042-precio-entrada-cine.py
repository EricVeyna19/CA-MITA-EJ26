# p042-precio-entrada-cine.py
# Descripcion del problema: Crea un programa para la taquilla de un cine que determine el precio de una entrada según la edad del
# cliente. El programa debe solicitar la edad y mostrar el precio correspondiente,

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---Bienvenido al cine---\n')
print('=' * 60)

print("Por favor Ingresa Tus datos")

edad = int(input("Ingresa tu edad: "))

if edad < 5:
    print("Tu entrada es gratis, Adelante.")

elif edad >= 5 and edad <= 12:
    print("El precio de tu entrada es de $5.")

elif edad >= 13 and edad <= 64:
    print("El precio de tu entrada es de $10.")

else:
    print("El precio de tu entrada es de $7.")