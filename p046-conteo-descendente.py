# p046-conteo-desendente.py
# Imprime numeros del 100 a 1 con while

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---Numeros de 100 a 1 con while---\n')
print('=' * 60)

r = 100

while r >= 1:
    print(r)
    r = r - 1

print(f'\nCiclo terminado: {r}')