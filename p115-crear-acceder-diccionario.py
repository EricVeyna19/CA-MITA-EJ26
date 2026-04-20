# p115-acceder-diccionario.py

print('\033[H\033[J')

dias = {
    1: 'Lunes',
    2: 'Martes',
    3: 'Miércoles',
    4: 'Jueves',
    5: 'Viernes',
    6: 'Sábado',
    7: 'Domingo'
}
print("Diccionario inicial:")
print(dias)

print("\nAccediendo a elementos:")

print(f"Llave 1 (con []): {dias[1]}")
print(f"Llave 7 (con []): {dias[7]}")

print(f"Llave 5 (con get()): {dias.get(5)}")
print(f"Llave 7 (con get()): {dias.get(7)}")

print("\nDiccionario final:")
print(dias)