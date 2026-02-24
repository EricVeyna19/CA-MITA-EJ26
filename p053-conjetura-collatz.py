# p053-conjetura-collatz.py
# Calcula la conjetura de Collatz
while True:
    print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
    print('=' * 60)
    print('---Imprime la conjetura de collatz---\n')
    print('=' * 60)

    while True:
        num = int(input('Dame un número = '))
        if num > 0: break
        print('Error, el número debe ser mayor que 0')
        
        
    print('\nLa conjetura de collatz es:')
    while True:
        if num == 1: break
        print(num,end=' ')
        if num % 2 == 0:

            num = num // 2

        else:

            num = num * 3 + 1

    print(num,end=' ')
    res=input('\n\nDeseas Continuar(S/N)? ').upper()
    if res=='N': break
    print('\nGracias por usar este programa. Vuelve pronto.')