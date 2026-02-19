# p045-conteo-ascendente.py
# Imprime numeros de 1 a n con while

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---Numeros de 1 a n con while---\n')
print('=' * 60)

n = int(input('Hasta donde ? ') ) # indica  el fin del ciclo
m = int(input('A que paso ? ') )  # indica los incrementos de cada ciclo

z= 0

while z <= n:
    print(z, end=' ')
    z = z + m

print(f'\nCiclo terminado en: {z}')