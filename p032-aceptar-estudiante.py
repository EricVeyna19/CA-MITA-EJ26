# p032-aceptar-estudiante.py
# Controla el acceso a la universidad en base a dos condiciones

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('--- Admisiones de la Universidad Patito ---')
print('=' * 60)

nombre = input("Dame tu nombre ? ")
edad = int(input('Edad ? '))

# Primer nivel: verificar la edad
if edad < 18:
    print(f'Lo sentimos {nombre}, solo permitimos mayores de 18')
else:
    # Si la edad es aceptable, pasar al siguiente nivel de verificación
    print('Ingresa 2 calificaciones:')
    cal1 = float(input('Calificación 1: '))
    cal2 = float(input('Calificación 2: '))

    # Segundo nivel: verificar las calificaciones
    if cal1 < 8 or cal2 < 8:
        print(f'Lo sentimos {nombre}, se requieren calificaciones mayores a 8')
    else:
        # Si ambas condiciones (edad y calificaciones) se cumplen
        print(f'{nombre} BIENVENIDO, tu edad y calificaciones lo permiten')

print('\nProceso terminado .. gracias por participar')