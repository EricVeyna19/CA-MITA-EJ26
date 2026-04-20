# p123-conjunto-personas.py

print('\033[H\033[J')

lista1 = ["Juan", "Maria", "Pedro", "Jose", "Rocio"]
lista2 = ["Pedro", "Juan", "Pablo", "Mateo", "Esther"]

A = set(lista1)
B = set(lista2)

print("Conjunto A:", A)
print("Conjunto B:", B)

print("\n--- Operaciones ---")

print("Unión (A | B):", A | B)

print("Intersección (A & B):", A & B)

print("Diferencia (A - B):", A - B)

print("Diferencia simétrica (A ^ B):", A ^ B)

print("\n--- Verificaciones ---")

print("¿Es {Pablo, Mateo} subconjunto de B?:", {"Pablo", "Mateo"}.issubset(B))

print("¿A es superconjunto de {Reynaldo, Angelica}?:", A.issuperset({"Reynaldo", "Angelica"}))

print("¿'Pedro' está en A?:", "Pedro" in A)

print("¿'Lilia' NO está en B?:", "Lilia" not in B)