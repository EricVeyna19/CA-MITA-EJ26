# p027-calcular-paga-extra.py
# Calcula la paga de un trabajador considerando horas extra.

print("\033[2J\033[H")
print('Calculando la paga de un trabajador ')

# Entrada de datos
print("Datos del trabajador: \n")
nombre = input('Nombre del trabajador: ')
horas = int(input('Horas trabajadas: '))
paga_hora = float(input('Paga por hora: '))

# Cálculo de la paga
if horas > 40:
    horas_normales = 40
    horas_extra = horas - 40
else:
    horas_normales = horas
    horas_extra = 0

paga_normal = horas_normales * paga_hora
paga_extra = horas_extra * (paga_hora * 2)
total = paga_normal + paga_extra

# Salida de resultados
print("\n--- Resultado del Cálculo ---")
print(f'El trabajador {nombre} trabajó {horas_normales} hrs normales y {horas_extra} hrs extra.')
print(f'Paga normal = ${paga_normal:13,.2f}')
print(f'Paga extra  = ${paga_extra:13,.2f}')
print(f'Total pagar = ${total:13,.2f}')

print('\n* ¡Programa finalizado! *')