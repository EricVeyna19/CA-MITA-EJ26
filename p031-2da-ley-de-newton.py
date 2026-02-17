# p031-2da-ley-de-newton.py
# calcula la fuerza, masa o aceleracion segun la ley de newton
print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('calcula la fuerza, masa o aceleracion segun la ley de newton\n')
print('=' * 60)

print(' [ F ] uerza      - f = m * a')
print(' [ M ] asa        - m = f / a')
print(' [ A ] Aceleracion - a = f / m')
op = input('Opcion ? ').upper()

if op == 'F':
    print('\nCalculando la Fuerza...')
    m = float(input('Masa (kg)        ? '))
    a = float(input('Aceleracion (m/s2) ? '))
    f = m * a 
    print(f'La Fuerza es : {f:.2f} N')

elif op == 'M':
    print('\nCalculando la Masa...')
    f = float(input('Fuerza (N)       ? '))
    a = float(input('Aceleracion (m/s2) ? '))
    if a != 0:
        m = f / a 
        print(f'La Masa es : {m:.2f} kg')
    else:
        print("Error: La aceleración no puede ser 0.")

elif op == 'A':
    print('\nCalculando la Aceleracion...')
    f = float(input('Fuerza (N) ? '))
    m = float(input('Masa (kg)   ? '))
    if m != 0:
        a = f / m  # Corregido: división en lugar de multiplicación
        print(f'La Aceleracion es : {a:.2f} m/s2')
    else:
        print("Error: La masa no puede ser 0.")

else:
    print(f'Opcion Invalida... "{op}" no es una opción.')

print('\nProceso terminado, gracias por utilizar este programa')