# p001-hola-mundo.py
# Lee datos y envia un saludo

print('Leyendo datos y enviando un saludo: \n')
# Entrada
nombre = input('Dame tu nombre ? ')
edad = int( input('Dame tu edad ? ') )
peso = float( input('Dame tu peso ? ') )
# Salida
print(f'{nombre} bienvenido a python, tu edad es {edad}, tu peso es {peso}')
print(type(nombre))
print(type(edad))
print(type(peso))