# p043-calculadora-anio-bisiesto.py
# Descripcion del problema: Escribe un programa que determine si un año, ingresado por el usuario, es bisiesto.

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---Caluculadora de año Bisiesto---\n')
print('=' * 60)


año = int(input("Ingresa un año: "))

if año % 400 == 0:
    print(f"El año {año} es bisiesto. (Porque es divisible por 400).")

elif año % 4 == 0 and año % 100 != 0:
    print(f"El año {año} es bisiesto. (Porque es divisible por 4 pero no por 100).")

elif año % 100 == 0:
    
    print(f"El año {año} no es bisiesto. (Porque es divisible por 100 pero no por 400).")

else:
    print(f"El año {año} no es bisiesto. (Porque no es divisible por 4).")