# p051-adivina-numero.py
# Permite al usuario advinar un numero generado al azar

print('\033[H\033[J')  # imprime una secuencia ansi que borra la pantalla
print('=' * 60)
print('---Permite al usuario advinar un numero generado al azar entre 1 y 50---\n')
print('=' * 60)

import random

numero_secreto = random.randint(1, 50) # Se elige un número entero al azar entre 1 y 50.
intento_usuario = 0
contador_intentos = 0

print(" ¡Bienvenido al juego 'Adivina el Número'! ")
print("He pensado en un número entre 1 y 50. ¿Podrás adivinarlo?")
print("------------------------------------------------------")

# Usamos 'while True' para que el juego continúe hasta que adivinemos el número y rompamos el ciclo con 'break'.
while True:
    intento_usuario = int(input("Tu número: "))
    contador_intentos += 1
    # Lógica de pistas
    if intento_usuario < numero_secreto:
        print(" ¡Demasiado bajo! Intenta con un número más alto.")
    elif intento_usuario > numero_secreto:
        print(" ¡Demasiado alto! Intenta con un número más bajo.")
    else:
    # Si no es ni más bajo ni más alto, ¡es el correcto!
        print(f"\n ¡Felicidades! ¡Adivinaste el número secreto que era {numero_secreto}!")
        print(f"Lo lograste en {contador_intentos} intentos.")
        # Usamos 'break' para terminar el juego.
        break