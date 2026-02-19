# p049-sumar-consecutivos.py
# Suma numeros hasta un total de 5000, pero cuenta hasta 200

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---Cuantos boletos tengo que vender para llegar a $5000---\n')
print('=' * 60)

n = int(input('Cuanto quieres recaudar ? ') )

b= 0
d = 0

while b < 200:
    b = b + 1
    d = d + b
    print(b, end= ' ')

    if d >= n:
        print('\nYa tengo el dinero me propuse !')
        break

if d < n:
    print(f'\n\n200 boletos no te alcanza para llegar a {n}, solo te alcanza para llegar a {d}')
else:
    print(f'\n\nUse {b} boletos para llegar a $ {d}')