# p103-ciudades.py
# Leer nombres de ciudades en una lista, continuando hasta que el usuario introduzca el carácter $. Imprimir:
# Cuántos elementos tiene la lista. La lista completa. La lista ordenada en orden descendente.
# Cuántas ciudades inician con una letra consonante y sus nombres.

print('\033[H\033[J')

ciudades = []

while True:
    ciudad = input("Introduzca nombre de ciudad ($ para detener): ")
    if ciudad == '$':
        break
    # Se agrega a la lista solo si no está vacía para evitar errores
    if ciudad.strip(): 
        ciudades.append(ciudad)

print("\n--- Resultados ---")
print(f"Total de ciudades introducidas: {len(ciudades)}")
print(f"Lista original: {ciudades}")

# Creamos una copia ordenada inversamente para no modificar la lista original
ciudades_descendente = sorted(ciudades, reverse=True)
print(f"\nLista ordenada descendente: {ciudades_descendente}")

# Filtramos las ciudades que inician con consonante
# Verificamos que sea una letra y que no sea una vocal (considerando mayúsculas, minúsculas y acentos)
vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
ciudades_consonante = [ciudad for ciudad in ciudades if ciudad[0].isalpha() and ciudad[0] not in vocales]

print(f"\nCiudades que inician con consonante: {len(ciudades_consonante)}")
print(f"Lista de ciudades con consonante inicial: {ciudades_consonante}")