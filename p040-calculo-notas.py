# p040-calculo-notas.py
# Descripcion del problema: Escribe un programa que calcule el promedio de 5 calificaciones ingresadas por el usuario. Basado en el
# promedio

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---CALCULO DE PROMEDIO DE NOTAS---\n')
print('=' * 60)

print("Ingresa las 5 calificaciones a promediar")

# Solicitar  el numero
cal1 = int(input("Primera  calificacion: "))
cal2 = int(input("Segunda  calificacion: "))
cal3 = int(input("Tercera  calificacion: "))
cal4 = int(input("cuarta   calificacion: "))
cal5 = int(input("Quinta   calificacion: "))

promedio = (cal1+cal2+cal3+cal4+cal5)/5

if promedio < 6: 
    print(f"Estas Reprobado, Tu promedio es de {promedio}")

elif promedio < 7: 
    print(f"Pasas de Panzazo, Tu promedio es de {promedio}")

elif promedio < 8:
    print(f"Bien, Tu promedio es de {promedio}, puedes mejorar")

elif promedio < 9:
    print(f"Muy bien, Tu promedio es de {promedio}, sigue asi")

elif promedio < 10:
    print(f"Excelente, Tu promedio es de {promedio}, sigue asi")

elif promedio == 10:
    print(f"Perfecto, Tu promedio es de {promedio}, Tu esfuerzo valio la pena")

else:
    print("Promedio invalido")

print("Fin del Programa")