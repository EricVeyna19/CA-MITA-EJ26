# p033-aceptar-estudiante-v2.py
# Controla el acceso a la universidad en base a dos condiciones

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('--- Admisiones de la Universidad Patito ---')
print('=' * 60)

nombre = input("Dame tu nombre ? ")
edad = int(input('Edad ? '))

if edad >= 18:
    print('Ingresa tus 2 calificaciones para continuar cada una con un enter:')
    # Agregamos etiquetas a los inputs para guiar al usuario
    cal1 = float(input('calificaciones 1: '))
    cal2 = float(input('calificaciones 2: '))

    if cal1 >= 8 and cal2 >= 8:
        print(f'\n¡Bienvenid@, {nombre}! Tu edad ({edad}) y tus calificaciones ({cal1}, {cal2}) permiten tu ingreso.')
    else:
        print(f'\nLo sentimos {nombre}, se requiere una calificación mínima de 8 en ambos calificaciones.')
else:
    print(f'\nLo sentimos, {nombre}. Solo aceptamos a mayores de 18 años.')

print('\nProceso terminado .. gracias por participar\n')