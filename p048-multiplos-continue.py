# p048-multiplos-continue.py
# Imprime solo los multiplos de n hasta 200

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---Imprime los multiplos de n a 200---\n')
print('=' * 60)

n = int(input('Que multiplos quieres hasta 200 ? ') )

c= 0

while c < 200:
    c= c + 1
    if c % n != 0 :
        continue
    print(f'{c} ', end='')