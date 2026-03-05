# p075-cifrado-cesar.py
# Cifra un mensaje usando el cifrado de Caesar

while True:
    print('\033[H\033[J') # Limpia la pantalla
    print('Cifra un mensaje usando el cifrado de Caesar\n')

    mensaje_original = input('Mensaje a encriptar : ')
    desplazamiento = int(input('Desplazamiento     : '))
    mensaje_cifrado = ""

    for caracter in mensaje_original:
        if caracter.isalpha():
            # Obtener el valor ASCII
            codigo_ascii = ord(caracter)
            
            # Definir la base (97 para 'a' minúscula, 65 para 'A' mayúscula)
            base = ord('a') if caracter.islower() else ord('A')
            
            # Aplicar la fórmula matemática del cifrado
            # $$nuevo\_codigo = base + (codigo\_ascii - base + desplazamiento) \pmod{26}$$
            codigo_nuevo = base + (codigo_ascii - base + desplazamiento) % 26
            mensaje_cifrado += chr(codigo_nuevo)
        else:
            # Si no es letra (espacios o símbolos), se queda igual
            mensaje_cifrado += caracter

    print(f'\nMensaje original: {mensaje_original}')
    print(f'Mensaje cifrado : {mensaje_cifrado}')

    if input('\n\n¿Deseas Continuar (S/N)? ').upper() == 'N':
        break

print('\nProceso terminado.')