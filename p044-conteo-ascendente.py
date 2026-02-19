# p044-conteo-ascendente.py
# Imprime numeros de 1 a 100 con while

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---Numeros de 1 a 100 con while---\n')
print('=' * 60)

z = 1

while z <= 100:
    print(z, end=' ')
    z = z + 1

print(f'\nCiclo terminado: {z}')