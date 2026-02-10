# p013-funciones-matematicas-precios.py
# Demostrar el uso de funciones matematicas para redondeo

import math as mt

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 40)
print('Demostra las funciones de redondeo en python' )
print('=' * 40)


precio = 15.65
print(f'Precio : {precio}')
print(f'Arriba : {mt.ceil(precio)}')
print(f'Abajo  : {mt. floor(precio) }')
print(f'Truncar: {mt.trunc(precio)}')
print(f'Normal : {round (precio) }')
print(f'2 Dec  : {round (precio, 2)}\n' )




