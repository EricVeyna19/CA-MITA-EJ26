# p125-segundo-examen-parcial.py
# Sistema de registro de vuelos - AeroRegistro

print("\033[H\033[J")  # Limpia pantalla

print("AeroRegistro - Sistema de Vuelos")
print("Captura de datos de los vuelos (* para terminar):\n")

# Lista principal donde se guardará cada vuelo como diccionario
vuelos = []

# =========================
# CAPTURA DE DATOS
# =========================
while True:
    numero_vuelo = input("Número de vuelo: ").strip()

    # Si el usuario escribe * o deja vacío, termina la captura
    if numero_vuelo == "*" or numero_vuelo == "":
        break

    origen = input("Origen: ").strip()
    destino = input("Destino: ").strip()
    aerolinea = input("Aerolínea: ").strip()

    # Validación para pasajeros
    while True:
        try:
            pasajeros = int(input("Pasajeros: "))
            if pasajeros < 0:
                print("Error: los pasajeros no pueden ser negativos.")
            else:
                break
        except ValueError:
            print("Error: captura un número entero para pasajeros.")

    # Validación para tarifa
    while True:
        try:
            tarifa = float(input("Tarifa: "))
            if tarifa < 0:
                print("Error: la tarifa no puede ser negativa.")
            else:
                break
        except ValueError:
            print("Error: captura un número válido para tarifa.")

    # Se crea el diccionario del vuelo
    vuelo = {
        "numero_vuelo": numero_vuelo,
        "origen": origen,
        "destino": destino,
        "aerolinea": aerolinea,
        "pasajeros": pasajeros,
        "tarifa": tarifa
    }

    # Se agrega a la lista principal
    vuelos.append(vuelo)
    print()

# =========================
# SALIDA DE DATOS
# =========================
print("\nDatos (Lista de diccionarios):")
print(vuelos)

# Si el usuario no capturó ningún vuelo, le avisa al usuario y termina
if len(vuelos) == 0:
    print("\nNo se registraron vuelos.")
else:
    print("\nTabla de datos:")
    print(f'{"No. Vuelo":<12}{"Origen":<18}{"Destino":<18}{"Aerolínea":<15}{"Pasajeros":<12}{"Tarifa":>12}')
    print("-" * 87)

    # Variables para el resumen
    conteo_aerolineas = {}
    conteo_destinos = {}
    suma_pasajeros = 0
    suma_tarifas = 0

    # Tomamos el primero como referencia inicial
    vuelo_mas_caro = vuelos[0]
    vuelo_mas_barato = vuelos[0]

    # Recorrido de todos los vuelos
    for vuelo in vuelos:
        print(f'{vuelo["numero_vuelo"]:<12}{vuelo["origen"]:<18}{vuelo["destino"]:<18}{vuelo["aerolinea"]:<15}{vuelo["pasajeros"]:<12}{vuelo["tarifa"]:>12,.2f}')

        # Acumulados
        suma_pasajeros += vuelo["pasajeros"]
        suma_tarifas += vuelo["tarifa"]

        # Conteo por aerolínea
        if vuelo["aerolinea"] in conteo_aerolineas:
            conteo_aerolineas[vuelo["aerolinea"]] += 1
        else:
            conteo_aerolineas[vuelo["aerolinea"]] = 1

        # Conteo por destino
        if vuelo["destino"] in conteo_destinos:
            conteo_destinos[vuelo["destino"]] += 1
        else:
            conteo_destinos[vuelo["destino"]] = 1

        # Buscar el vuelo más caro
        if vuelo["tarifa"] > vuelo_mas_caro["tarifa"]:
            vuelo_mas_caro = vuelo

        # Buscar el vuelo más barato
        if vuelo["tarifa"] < vuelo_mas_barato["tarifa"]:
            vuelo_mas_barato = vuelo

    # Cálculos finales
    total_vuelos = len(vuelos)
    promedio_pasajeros = suma_pasajeros / total_vuelos
    promedio_tarifas = suma_tarifas / total_vuelos

    # =========================
    # RESUMEN
    # =========================
    print("\nResumen:")
    print(f"Vuelos totales: {total_vuelos}")

    print("\nAerolíneas:")
    for aerolinea, cantidad in conteo_aerolineas.items():
        print(f"• {aerolinea}: {cantidad}")

    print("\nDestinos:")
    for destino, cantidad in conteo_destinos.items():
        print(f"• {destino}: {cantidad}")

    print(f"\nPasajeros -> Suma: {suma_pasajeros}, Promedio: {promedio_pasajeros:.2f}")
    print(f"Tarifa -> Suma: {suma_tarifas:,.2f}, Promedio: {promedio_tarifas:,.2f}")

    print(
        f'{vuelo_mas_caro["numero_vuelo"]} de ${vuelo_mas_caro["tarifa"]:,.2f} es el más caro, '
        f'{vuelo_mas_barato["numero_vuelo"]} de ${vuelo_mas_barato["tarifa"]:,.2f} es el más barato.'
    )