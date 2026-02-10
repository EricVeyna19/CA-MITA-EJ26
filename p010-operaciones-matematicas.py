# Demuestra el uso de los diferentes operadores aritmeticos

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 50)
print('CALCULADORA DE OPERACIONES MATEMATICAS')
print('=' * 50)

x = float(input('Dame el valor de x : '))
y = float(input('Dame el valor de y : '))

print(f'Los valores de X y Y son: {x} {y}')
print('-' * 40)

# Mostrar resultado de las operaciones directamente, con formato alineado
print(f'Suma : {x:>6} + {y:>6} = {x + y:>10.2f}')
print(f'Resta: {x:>6} - {y:>6} = {x - y:>10.2f}')
print(f'Mult : {x:>6} * {y:>6} = {x * y:>10.2f}')
print(f'Divi : {x:>6} / {y:>6} = {x / y:>10.2f}')
print(f'Mod  : {x:>6} % {y:>6} = {x % y:>10.2f}')
print(f'Exp  : {x:>6} ** {y:>6} = {x ** y:>10.2f}')
print(f'Div E: {x:>6} // {y:>6} = {x // y:>10.2f}')

print('-' * 50)