# p119-procesar-diccionario.py

print('\033[H\033[J')

nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

nomina = dict(zip(nombres, sueldos))

print("Diccionario de nómina:")
print(nomina)

print("\n--- Iterando llaves (keys) ---")
for nombre in nomina.keys():
    print(nombre)

print("\n--- Iterando valores (values) ---")
for sueldo in nomina.values():
    print(sueldo)

print("\n--- Iterando llave y valor (usando llave) ---")
for nombre in nomina:
    print(f"{nombre} -> {nomina[nombre]}")

print("\n--- Iterando llave y valor (items) ---")
for nombre, sueldo in nomina.items():
    print(f"({nombre}, {sueldo})")

suma_total = sum(nomina.values())
promedio = suma_total / len(nomina)

print("\n--- Cálculos ---")
print(f"Suma total de sueldos: {suma_total}")
print(f"Promedio de sueldos: {promedio:.2f}")