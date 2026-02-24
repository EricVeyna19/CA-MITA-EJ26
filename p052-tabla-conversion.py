# p052-tabla-conversion.py
# Muestra una tabla de conversion de Peso a Dollar

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---Tabla de Conversion Peso a Dollar---\n')
print('=' * 60)


tc = 20.71
while True :
    print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
    print('=' * 60)
    print('---Tabla de Conversion Peso a Dollar---\n')
    print('=' * 60)
    print(f'Tipo de Cambio: {tc} Pesos por Dollar')
    print("-"*60)
    while True:
        pi = float(input("Valor inicial: "))
        pf = float(input("Valor final : "))
        if (pi>0 and pf>0) and pi<pf:

            break

        print("Error en los valores, intente de nuevo")
    c = pi
    print("\nPesos\tDollar")
    print("-"*15)
    while c<=pf :
        print(f'{c}\t{c/tc:.2f}')
        c+=1
    print("-"*60)
    res=input('Deseas Continuar(S/N)? ').upper()
    if res=='N':
        break