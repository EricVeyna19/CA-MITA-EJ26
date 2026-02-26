"""
Objetivo: Gestionar ventas de fotocopias aplicando el descuento sobre el total final.
Desarrollador: Asistente
"""

# --- ENTRADAS ---
ventas_realizadas = 0
cant_C = 0; orig_C = 0.0
cant_O = 0; orig_O = 0.0
cant_D = 0; orig_D = 0.0
cant_P = 0; orig_P = 0.0

print('\033[H\033[J')
print('---------------------------------')
print("Papelería la Malena, SA de CV.")
print("Sistema de ventas de copias")
print('---------------------------------')
continuar = 'S'

# --- PROCESO ---
while continuar.upper() == 'S':
    ventas_realizadas += 1
    print(f"\nVenta: {ventas_realizadas}")
    tipo = input("Tipo de copia (C)arta $3, (O)ficio $4, (D)oble Of $6, (P)lano $12 ? ").upper()
    cantidad = int(input("Cantidad ? "))

    precio = 0.0
    
    if tipo == 'C': precio = 3.00
    elif tipo == 'O': precio = 4.00
    elif tipo == 'D': precio = 6.00
    elif tipo == 'P': precio = 12.00
    else:
        print("Tipo de copia no válido.")
        ventas_realizadas -= 1
        continue

    costo_base = precio * cantidad

    # Sumamos cantidades y costos originales
    if tipo == 'C': cant_C += cantidad; orig_C += costo_base
    elif tipo == 'O': cant_O += cantidad; orig_O += costo_base
    elif tipo == 'D': cant_D += cantidad; orig_D += costo_base
    elif tipo == 'P': cant_P += cantidad; orig_P += costo_base

    continuar = input("Otra venta (S/N) ? ")

# --- CÁLCULOS FINALES Y SALIDAS ---
total_copias = cant_C + cant_O + cant_D + cant_P
total_original = orig_C + orig_O + orig_D + orig_P

# Aplicar descuento sobre el total de todas las compras
if total_copias > 50:
    dinero_descontado = total_original * 0.10
    porcentaje_desc = 10
else:
    dinero_descontado = 0.0
    porcentaje_desc = 0

total_pagar = total_original - dinero_descontado
print('---------------------------------') 
print("\n--- Resumen diario de ventas ---")
print('---------------------------------') 
print(f"Ventas realizadas: {ventas_realizadas}")

print(f"Carta     : {cant_C:<4} $ {orig_C:.2f}")
print(f"Oficio    : {cant_O:<4} $ {orig_O:.2f}")
print(f"Doble Of. : {cant_D:<4} $ {orig_D:.2f}")
print(f"Plano     : {cant_P:<4} $ {orig_P:.2f}")

print("-" * 45)
print(f"Cantidad Original : $ {total_original:.2f}")
print(f"Descuento Total   : $ {dinero_descontado:.2f} ({porcentaje_desc}%)")
print(f"Total a Pagar     : $ {total_pagar:.2f} por {total_copias} copias")
print("-" * 45)

if total_pagar < 50.00:
    mensaje = "Venta moderada"
elif 50.00 <= total_pagar <= 150.00:
    mensaje = "Venta frecuente"
else:
    mensaje = "Venta superada"

print(f"Esta venta es una {mensaje}")