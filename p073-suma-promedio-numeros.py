# p073-suma-promedio-numeros.py
# Suma de n numeros introducidos por el usuario usando ciclo for

while(True):
    print('\033[H\033[J')
    cuantos = int(input('¿Cuántos números deseas procesar? '))
    
    if cuantos > 0:
        suma = 0
        cadnum = ""
        
        for i in range(1, cuantos + 1):
            n = int(input(f'Número[{i}] = '))
            suma += n
            cadnum = cadnum + ' ' + str(n)

        promedio = suma / cuantos
        print(f'\nLos números que introdujiste fueron: {cadnum}')
        print(f'La suma es {suma}, el promedio es {promedio}')
    else:
        print("La cantidad debe ser mayor a 0.")

    if input('\n¿Deseas continuar (S/N)? ').upper() == 'N': 
        break

print('\nHemos llegado al final ....')