# p129-func-param-nombre.py

print('\033[H\033[J')

def saluda(apaterno: str, amaterno: str, nombre: str) -> None:
    print(f'Hola {nombre} {apaterno} {amaterno}')

saluda('Lopez', 'Martinez', 'Ana')
saluda(nombre='Ana', amaterno='Martinez', apaterno='Lopez')