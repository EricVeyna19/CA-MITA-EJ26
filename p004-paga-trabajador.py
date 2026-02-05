# p004-paga-trabajador.py
# calcula la paga de un trabajador

print('Calculando la paga de un trabajador')
#Entrada
nombre = input('Nombre > ')
horas = int(input('Horas trabajadas > '))
paga = float(input('Paga x hora > ') )
#proceso
tasa = 0.3
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta= pagabruta - impuesto
#salida
print('Resumen de pagos : \n')
print(f'El trabajador {nombre}, trabajo {horas} horas, con una paga de {paga} pesos, impuesto de {tasa} %')
print(f'Paga Bruta : {pagabruta}')
print(f'Impuesto : {impuesto}')
print(f'paga neta : {paganeta}')
