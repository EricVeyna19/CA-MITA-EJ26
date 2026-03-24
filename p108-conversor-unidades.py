# p108-conversor-unidades.py
# Conversor de unidades de medida (A prueba de errores)

conversiones = {
    'km': 1000,
    'm': 1,
    'cm': 0.01,
    'mm': 0.001
}

print('\033[H\033[J')
print('\nConversor de unidades de medida')

# Validar que la longitud sea un número
while True:
    try:
        long = float(input('Dame la longitud ? '))
        break # Sale del ciclo si es correcto
    except ValueError:
        print('Error: Debe ser un número. Intenta de nuevo.')

# Validar que la unidad exista en el diccionario
while True:
    unidad = input('Unidad (km, m, cm, mm) ? ').lower()
    if unidad in conversiones: 
        break
    print('Error: Unidad no válida. Intenta de nuevo.')

#  Calcular y mostrar el resultado
res = long * conversiones[unidad]

print(f'\nUna longitud de {long} {unidad} equivale a {res:.2f} metros.')