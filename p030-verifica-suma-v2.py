# p030-verifica-suma-v2.py
# Verifica si la suma de dos numeros es igual a un tercero
print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('Verifica si la suma de dos numeros es igual a un tercero\n')
print('=' * 60)

# Asignar y convertir las entradas a enteros

print('Dame 3 numeros enteros separados por espacio ')
n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

# Evaluar las posibles combinaciones con if/elif

# Evaluar las posibles combinaciones con if/elif
if n1 + n2 == n3:
    print(f' n1 + n2 es igual a n3 ({n1} + {n2} = {n3})')
elif n1 + n3 == n2:
    print(f' n1 + n3 es igual a n2 ({n1} + {n3} = {n2})')
elif n2 + n3 == n1:
    print(f' n2 + n3 es igual a n1 ({n2} + {n3} = {n1})')
elif n2 == n3 == n1 :
    print(f'{n1} ={n2} = {n3}')
else:
    # Si ninguna de las condiciones anteriores se cumple
    print(' Ninguna combinación de suma es igual al tercer número.')