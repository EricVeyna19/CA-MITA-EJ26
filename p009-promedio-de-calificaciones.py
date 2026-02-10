# p009-promedio-de-calificaciones
# Calcula el promedio de tres calificaciones ingresadas por el usuario

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 50)
print('CALCULANDO EL PROMEDIO DE TRES CALIFICACIONES')
print('=' * 50)

# Solicitar las calificaciones en una sola línea separadas por espacio
print('Dame 3 calificaciones separadas por espacio')
cal1, cal2, cal3 = input().split()
call, cal2, cal3 = int(cal1), int(cal2), int(cal3)

# Calcular promedio

suma = call + cal2 + cal3
promedio = suma / 3

# Mostrar resultado
print(f'Las calificaciones fueron: {cal1} {cal2} {cal3}')
print(f'La suma de las calificaciones es: {suma}')
print(f'El promedio de las calificaciones es : {promedio:.2f}\n')


