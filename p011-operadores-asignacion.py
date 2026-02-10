#p011-operadores-asignacion.py
# Demuestra el uso de operadores de asignacion

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 40)
print('OPERADORES DE ASIGNACION EN PYTHON' )
print('=' * 40)

# Operador de asignacion basico
x = 10
print(f'X = {x}')

# Aplicar difrentes operadores de asignacion
x += 5 ; print(f'x += 5 -> x = {x} ' )
x -= 3 ; print(f'x -= 3 -> x = {x} ' )
x *= 2 ; print(f'x *= 2 -> x = {x} ' )
x /= 4 ; print(f'x /= 4 -> x = {x} ' )
x **= 2 ; print(f'x **= 2 -> x = {x}' )
x %= 5 ; print(f'x %= 5 -> x = {x} ' )
x //= 2 ; print(f'x //= 5 -> x = {x}' )

print('=' * 40)