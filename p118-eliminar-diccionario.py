# p118-eliminar-diccionario.py
print('\033[H\033[J')

municipios = {
    "Apozol": 1863,
    "Calera": 1868,
    "Fresnillo": 1554,
    "Guadalupe": 1821,
    "Jalpa": 1824,
    "Jerez": 1824,
    "Loreto": 1931,
    "Mazapil": 1824,
    "Momax": 1857
}

print("Diccionario inicial:")
print(municipios)

del municipios["Apozol"]
print("\nDespués de eliminar 'Apozol':")
print(municipios)

municipios.pop("Fresnillo")
print("\nDespués de pop('Fresnillo'):")
print(municipios)

municipios.popitem()
print("\nDespués de popitem() (elimina el último elemento):")
print(municipios)

municipios.clear()
print("\nDespués de clear():")
print(municipios)