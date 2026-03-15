# p082-compara-rendimiento-inversion.py
# Descripcion del problema: Desarrolla un programa que compare el crecimiento de dos fondos de inversión a lo largo de varios años. 
# El usuario debe ingresar el monto inicial y la tasa de interés anual (porcentaje) para cada uno de los dos fondos, así como 
# el número de años a proyectar. El programa deberá mostrar una tabla comparativa anual y al final indicar qué fondo 
# generó un mayor rendimiento.

print("\033[H\033[J")
print("--- Fondo de Inversión A ---")
monto_a = float(input("Ingresa el Monto inicial: "))
tasa_a = float(input("Ingresa la Tasa de interés anual (%): "))

print("\n--- Fondo de Inversión B ---")
monto_b = float(input("Ingresa el Monto inicial: "))
tasa_b = float(input("Ingresa la Tasa de interés anual (%): "))

años = 0
# Ciclo while para validar que los años sean correctos
while años <= 0:
    años = int(input("\nIngresa el numero de Años a proyectar: "))
    if años <= 0:
        print("Ingresa un número Valido.")

print("\n--- Comparación de Rendimientos Anuales ---")
print("Año | Fondo A          | Fondo B")
print("-" * 45)

# Ciclo for para calcular el crecimiento año con año
for año in range(1, años + 1):
    monto_a = monto_a + (monto_a * (tasa_a / 100))
    monto_b = monto_b + (monto_b * (tasa_b / 100))
    # Formato para que los números queden alineados como en la imagen
    print(f"{año:<3} | $ {monto_a:>12.2f} | $ {monto_b:>12.2f}")

print()

# Condicional if para comparar quién ganó
if monto_a > monto_b:
    print(f"Resultado final: El Fondo A (${monto_a:.2f}) superó al Fondo B (${monto_b:.2f}).")
elif monto_b > monto_a:
    print(f"Resultado final: El Fondo B (${monto_b:.2f}) superó al Fondo A (${monto_a:.2f}).")
else:
    print(f"Resultado final: Ambos fondos empataron con (${monto_a:.2f}).")