# p092-lista-de-gastos.py
# Permite llevar el control de una lista de gastos mensuales

print('\033[H\033[J')

gastos = [450.50, 120.00, 85.90, 230.00, 55.75]
limite_gasto = 100.00

while True:
    print("\n--- Menu de Gestion de Gastos ---")
    print("1. Ver todos los gastos")
    print("2. Agregar un nuevo gasto")
    print("3. Modificar un gasto existente")
    print("4. Eliminar un gasto (por reembolso o error)")
    print("5. Ver resumen y total de gastos")
    print("6. Salir")
    
    opcion = input('Elige una opcion (1-6) : ')
    
    if opcion == '1':
        print(f'\nTodos los gastos: {gastos}')
        
    elif opcion == '2':
        nuevo_gasto = float(input('Nuevo Gasto ? '))
        gastos.append(nuevo_gasto)
        print('Gasto agregado exitosamente.')
        
    elif opcion == '3':
        pos = int(input('Posicion del gasto a modificar (indice empieza en 0) ? '))
        if 0 <= pos < len(gastos):
            nuevo_valor = float(input('Nuevo valor? '))
            gastos[pos] = nuevo_valor
            print('Gasto modificado exitosamente.')
        else:
            print('Error: Posicion no encontrada en la lista.')
            
    elif opcion == '4':
        gasto_eliminar = float(input('Gasto a eliminar ? '))
        if gasto_eliminar in gastos:
            gastos.remove(gasto_eliminar)
            print('Gasto eliminado exitosamente.')
        else:
            print('Error: Gasto no encontrado en la lista.')
            
    elif opcion == '5':
        total_gastado = 0
        print('\nGastos del mes:')
        for gasto in gastos:
            total_gastado += gasto
            if gasto > limite_gasto:
                print(f'Gasto excede limite: {gasto}')
            else:
                print(f'Gasto normal: {gasto}')
        print(f'Total gastado : {total_gastado}')
        
    elif opcion == '6':
        print('\nGracias por utilizar este sistema')
        break
        
    else:
        print('\nError: Opcion NO VALIDA. Intenta de nuevo.')