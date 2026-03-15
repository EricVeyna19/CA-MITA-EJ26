# p086-triangulo-invertido-numeros.py
# Solicitar al usuario un número entero n que determinará la altura de un triángulo 
# numérico invertido. El programa debe imprimir n renglones. El primer renglón 
# contendrá los números de 1 a n, el segundo de 1 a n-1, y así sucesivamente 
# hasta que el último renglón contenga solo el número 1.

print("\033[H\033[J")

n = int(input("Dame un numero: "))

# El ciclo principal va desde n hasta 1, restando 1 en cada paso
for i in range(n, 0, -1):
    # El ciclo interno imprime los números desde 1 hasta el valor actual de i
    for j in range(1, i + 1):
        print(j, end=" ")
    # Salto de línea al terminar cada renglón
    print()