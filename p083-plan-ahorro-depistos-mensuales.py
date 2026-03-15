# p083-plan-ahorro-depositos-mensuales.py
# El programa simulará un plan de ahorro. Deberá solicitar al usuario un monto inicial, 
# un depósito mensual fijo, una tasa de interés mensual (porcentaje), y el número total 
# de meses del plan. El programa debe mostrar una tabla que detalle, para cada mes, 
# el saldo inicial, el interés ganado en ese mes, y el saldo final. El interés se calcula 
# sobre el saldo inicial antes de sumar el nuevo depósito.

print("\033[H\033[J")

monto_inicial = float(input("Ingresa el Monto inicial de ahorro: "))
deposito_mensual = float(input("Ingresa el Deposito mensual: "))
tasa_interes = float(input("Ingresa la tasa de interes mensual (%): "))
meses = int(input("Numero de meses a simular: "))

print("\n--- Plan de Ahorro Detallado ---")

saldo_actual = monto_inicial

for mes in range(1, meses + 1):
    interes_ganado = saldo_actual * (tasa_interes / 100)
    saldo_final = saldo_actual + interes_ganado + deposito_mensual
    
    print(f"Mes {mes}: Saldo Inicial: {saldo_actual:.2f} | Interes: {interes_ganado:.2f} | Saldo Final: {saldo_final:.2f}")
    
    saldo_actual = saldo_final

print(f"\nAl final de {meses} meses, tendras {saldo_actual:.2f}")