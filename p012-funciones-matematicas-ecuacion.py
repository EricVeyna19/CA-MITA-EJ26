# p012-funcion-matematicas-equacion.py
# Evaluar la función f(x, y) = 3x² + √(x² + y²) + e^(ln(x))
# Usando operadores de exponenciacion y la funcion pow

import math as mt      # Importar la biblioteca math para funciones matemáticas con un alias

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 40)
print('EVALUAR LA EXPRESION: f(x, y) = 3x² + √(x² + y²) + e^(ln(x) EN PYTHON' )
print('=' * 40)

x = float (input ('Dame X : '))
y = float (input ('Dame Y : ' ) )

fxy_exp = 3 * x**2 + mt.sqrt(x**2 + y**2) + mt.exp(mt.log(x))
fxy_pow = 3 * mt.pow(x,2) + mt.sqrt(mt.pow(x,2) + mt.pow(y,2)) + mt.exp(mt.log(x))

print(f'El resutaldo es f({x}, {y} usando el operador ** es: )= {fxy_exp:.2f}')
print(f'El resutaldo es f({x}, {y} usando la funciones pow es: )= {fxy_pow:.2f}\n')


