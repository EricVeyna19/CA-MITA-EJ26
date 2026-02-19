# p050-conteo-numeros.py
# Lee y cuenta numeros hasta que se introduce 999

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---Lee y cuenta numeros hasta que se introduce 999---\n')
print('=' * 60)

s = c = cp = cn = cz = 0

while True:
    num = int(input('Numero ? ') )
    if num == 999:
        break
    c += 1
    s += num
    if num > 0 :
        cp+=1
    elif num < 0 :
        cn+=1
    else:
        cz+=1

print('\nReporte Final')
print(f'Fueron : {c} numeros')
print(f'Suma   : {s} ')
print(f'Pos    : {cp}')
print(f'Neg    : {cn}')
print(f'Cer    : {cz}')