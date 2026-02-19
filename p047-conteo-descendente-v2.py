# p047-conteo-desendente.py
# Imprime numeros del n a 1 con while

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---Numeros de n a 1 con while---\n')
print('=' * 60)

n = int(input('Desde donde ? ') )
m = int(input('En decrementos de ? ') )
r = n

while r >= 1:
    print(r)
    r =r-m

print(f'\nCiclo terminado: {r}')