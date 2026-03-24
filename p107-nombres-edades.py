# p107-nombres-edades.py
# Gestión de nombres y edades usando diccionarios

print('\033[H\033[J')

print('Gestión de nombres y edades usando diccionarios\n')
datos = {}

print('Introduce nombres y edades (deja el nombre vacío para terminar)')

#Ciclo para pedir datos
while True:
    nombre = input('Dame el nombre?')
    if nombre == '':
        break # Detiene el ciclo si no se escribe nada
    else:
        # Guarda la edad convirtiéndola a número entero (int)
        datos[nombre] = int(input('Edad?'))

print(f'\nEl diccionario de datos creado: \n{len(datos)} - {datos}\n')

#Calcular suma y promedio
print('\nListado y promedio de edades:')
s = 0

for n, e in datos.items():
    print(f'{n:<20} - {e:2}')
    s += e

# Validación para evitar error si el diccionario está vacío
if len(datos) > 0:
    p = s / len(datos)
    print(f'\n\nSuma: {s} y promedio: {p:.2f}')
else:
    print('\n\nNo se ingresaron datos.')