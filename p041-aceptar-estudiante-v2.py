# p041-aceptar-estudiante-v2
# Descripcion del problema: La "Universidad Kitty Kat SA" solo acepta estudiantes que cumplan con los siguientes requisitos: ser 
# mujer, ser mayor de 21 años y tener un promedio entre 8 y 9.5. 
# Escribe un programa que solicite el nombre, sexo (h/m), edad y tres calificaciones de un aspirante. El programa 
# debe evaluar los datos y mostrar un mensaje claro que indique si el estudiante fue aceptado. Si no es aceptado, el
# mensaje debe especificar la razón del rechazo (ya sea por no cumplir con el sexo, la edad o el promedio requerido).

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 80)
print('---Criterios de aceptacion para Universidad Kitty Kat SA---\n')
print('=' * 80)

print("Por favor Ingresa Tus datos")

nombre = input("Nombre del aspirante: ")
sexo = input("Sexo (h/m): ")
edad = int(input("Edad: "))

print("Ingresa 3 calificaciones a promediar")

cal1 = float(input("Calificación 1: "))
cal2 = float(input("Calificación 2: "))
cal3 = float(input("Calificación 3: "))

print('=' * 80)
print('---DATOS INGRESADOS---\n')
print('=' * 80)
print(f"Nombre          : {nombre}")
print(f"Sexo            : {sexo}")
print(f"Edad            : {edad}")
print(f"Calificaciones  : {cal1}, {cal2}, {cal3}")
print('=' * 80)

promedio = (cal1 + cal2 + cal3) / 3

if sexo != "m":
    print(f"Lo sentimos {nombre}, fuiste rechazado. Dedes de ser mujer para ingresar.")

elif edad <= 21:
    print(f"Lo sentimos {nombre}, fuiste rechazada. Debes ser mayor de 21 años para ingresar.")

elif promedio < 8 or promedio > 9.5:
    print(f"Lo sentimos {nombre}, fuiste rechazada. Tu promedio ({promedio:.2f}) no está entre 8 y 9.5.")

else:
    print(f"¡Felicidades {nombre}! Has sido aceptada en la Universidad Kitty Kat SA.")
    print(f"Tu promedio: {promedio:.2f} esta dentro del rango")

print('=' * 80)