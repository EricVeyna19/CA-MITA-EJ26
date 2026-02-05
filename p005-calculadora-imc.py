# p005-calculadora-imc.py
# Calcular el IMC de una persona

print('Calculando el indice de masa corporal (IMC) : \n')

Peso_k = float(input('Dame tu peso en Kilogramos: ') )
altura_m = float(input('Dame tu altura en metros: ') )

imc = Peso_k / (altura_m ** 2) # El asterisco doble es un operador aritmetico que eleva un numero a una potencia

print(f'Si tienes un peso de {Peso_k} y una altura de {altura_m} tu IMC es {imc:.2f}')