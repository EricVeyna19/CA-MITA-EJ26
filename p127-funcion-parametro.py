# p127-funcion-parametro.py

print('\033[H\033[J')

def saluda(nombre: str) -> None:
    print(f'Hola {nombre} bienvenido a Python, tu nombre tiene {len(nombre)} caracteres')

saluda('Eric Veyna')
saluda('Juan el del saguan')
saluda('María Benita')