# p061-suma-200.py
# Descripcion del problema: Leer números y sumarlos hasta que el total acumulado sea mayor o igual a 200. Al terminar, mostrar cuántos
# números se introdujeron y la suma final.

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---Leer números y sumarlos hasta que el total acumulado sea mayor o igual a 200.---\n')
print('=' * 60)

continuar = 'S'

while continuar.upper() == 'S':
    suma = 0
    conteo = 0

    while suma <= 200:
        numero = int(input(f"Suma actual: {suma}. Introduce un número: "))
        suma += numero
        conteo += 1

    print("--------------------")
    print("Meta de 200 alcanzada.")
    print(f"Suma final: {suma}")
    print(f"Total de números introducidos: {conteo}")

    continuar = input("\n¿Desea continuar (S/N)? ")