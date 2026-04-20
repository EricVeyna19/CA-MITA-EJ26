# p124-conjunto-numeros.py

print('\033[H\033[J')

lista1 = [50, 60, 70, 80, 90, 100, 200]
lista2 = [60, 90, 100, 300, 400, 500]
lista3 = [10, 20, 60, 90, 70, 100, 600, 700]

A = set(lista1)
B = set(lista2)
C = set(lista3)

print("Conjunto A:", A)
print("Conjunto B:", B)
print("Conjunto C:", C)

print("\n--- Operaciones ---")

print("Unión (A | B):", A | B)

print("Unión (B | C):", B | C)

print("Diferencia (A - C):", A - C)

print("Diferencia simétrica (B ^ C):", B ^ C)

print("Intersección (B & C):", B & C)

print("\n--- Verificaciones ---")

print("¿A es subconjunto de B?:", A.issubset(B))
print("¿C es subconjunto de A?:", C.issubset(A))
print("¿Está el número 100 en A?:", 100 in A)
print("¿Está el número 60 en A, B y C?:", 60 in A and 60 in B and 60 in C)
print("¿No está el número 900 en C?:", 900 not in C)