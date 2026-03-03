"""
Objetivo:          Aprender a resolver problemas mediante el lenguaje de programacion Python
Nombre del Alumno: Eric Gaspar Veyna
Matrícula:         34150348
Materia:           Computación Aplicada - MITA
Examen:            Primer Parcial
"""

# --- Inicialización de Contadores y Acumuladores ---
# Aquí se declaran todas las variables que necesitarás para guardar los datos

# --- Contadores de Asistentes ---
total_estudiantes   = 0
total_adultos       = 0
total_tercera_edad  = 0
total_academicos    = 0
# ... (agrega los demás contadores de tipo de comprador y de sexo)
total_hombres    = 0
total_mujeres    = 0
total_asistentes = 0
total_rechazados = 0
suma_edades      = 0

# --- Acumuladores de Ingresos ---
ingresos_estudiantes  = 0.0
ingresos_adultos      = 0.0
ingresos_tercera_edad = 0.0
ingresos_academicos   = 0.0
# ... (agrega los demás acumuladores de ingresos)

ingresos_totales = 0.0

# --- Precios de los Boletos (constantes) ---
PRECIO_ESTUDIANTE  = 50.0
PRECIO_ADULTO      = 90.0
PRECIO_TERCERA     = 60.0
PRECIO_ACADEMICO   = 70.0
# ... (agrega las demás constantes de precios)

print('\033[2J\033[H')
print("--- Sistema de Venta de Boletos de Cine ---")

# --- Ciclo Principal para la Venta de Boletos ---
# Usaremos un ciclo while para registrar ventas hasta que el usuario decida parar.
numero_venta = 1
continuar_venta = "s"
while continuar_venta == "s" or continuar_venta == "S":

    print("\n--- Nueva Venta ---")
    # --- 1. Solicitud de Datos ---
    # Pide la edad, el tipo de comprador y el sexo.
    # ¡Recuerda convertir la edad a un número entero!
    edad = int(input("  Ingresa tu Edad: "))

    # --- 2. Validación de Edad (Clasificación B) ---
    # La película es para mayores de 13 años.
    if edad > 13:
        print("  Tipo de comprador:")
        print("    1. Estudiante")
        print("    2. Adulto")
        print("    3. Tercera Edad")
        print("    4. Académico")
        tipo = int(input("  Elige una opción (1-4): "))

        if tipo == 1:
            tipo_nombre = "Estudiante"
            precio      = PRECIO_ESTUDIANTE
        elif tipo == 2:
            tipo_nombre = "Adulto"
            precio      = PRECIO_ADULTO
        elif tipo == 3:
            tipo_nombre = "Tercera Edad"
            precio      = PRECIO_TERCERA
        elif tipo == 4:
            tipo_nombre = "Académico"
            precio      = PRECIO_ACADEMICO
        else:
            tipo_nombre = "Desconocido"
            precio      = 0

        # --- 4. Solicitud de Sexo ---
        print("  Sexo:")
        print("    1. Hombre")
        print("    2. Mujer")
        sexo_op = int(input("  Elige una opción (1-2): "))

        if sexo_op == 1:
            sexo_nombre = "Hombre"
        else:
            sexo_nombre = "Mujer"

        # Si la edad es permitida, procede con la venta.
        # Muestra el mensaje de bienvenida con los datos registrados
        print(f"¡Bienvenido(a)!... Edad {edad}, Sexo {sexo_nombre}, Tipo {tipo_nombre}.\n")
        
        # --- 3. Actualización de Estadísticas Generales ---
        # Incrementa el contador de asistentes y suma la edad para el promedio.
        total_asistentes += 1
        suma_edades      += edad

        # Incrementa el contador de sexo correspondiente (hombre o mujer).
        if sexo_op == 1:
            total_hombres += 1
        else:
            total_mujeres += 1

        # --- 4. Cálculo de Costo y Actualización de Contadores Específicos ---
        # Usa una estructura if/elif/else para determinar el precio y actualizar
        # los contadores del tipo de comprador y sus ingresos.
        # Suma el costo del boleto a los ingresos totales.

        if tipo == 1:
            total_estudiantes  += 1
            ingresos_estudiantes += precio
        elif tipo == 2:
            total_adultos      += 1
            ingresos_adultos   += precio
        elif tipo == 3:
            total_tercera_edad      += 1
            ingresos_tercera_edad   += precio
        elif tipo == 4:
            total_academicos    += 1
            ingresos_academicos += precio

    else:
        # Si la edad no es permitida, muestra un mensaje y actualiza el contador ()
        print("ACCESO DENEGADO: El comprador es menor de 13 años.")
        # ... (incrementa el contador de personas rechazadas)
        total_rechazados += 1

    # Pregunta al usuario si desea registrar otra venta.
    numero_venta   += 1
    continuar_venta = input("\n¿Deseas registrar otra venta? (S/N): ")


# --- FIN DEL CICLO ---

# --- 5. Cálculo de Promedio ---
# Calcula el promedio de edad. Cuidado con la división entre cero si no hubo asistentes.
# if total_asistentes > 0:
#     promedio_edad = ... # (calcula el promedio aquí)

if total_asistentes > 0:
    promedio_edad = suma_edades / total_asistentes
else:
    promedio_edad = 0

ingresos_totales = (ingresos_estudiantes + ingresos_adultos + ingresos_tercera_edad + ingresos_academicos)

# --- 6. Impresión del Reporte Final ---
print("\n*** REPORTE FINAL DE LA FUNCIÓN ***")

print("\n--- Estadísticas del Público ---")
# Imprime todos los totales de asistentes por tipo y sexo.
print(f"Total de Estudiantes:  {total_estudiantes}")
print(f"Total de Adultos:      {total_adultos}")
print(f"Total de Tercera Edad: {total_tercera_edad}")
print(f"Total de Académicos:   {total_academicos}")
print("-------------------------------")
print(f"Total de Hombres: {total_hombres}")
print(f"Total de Mujeres: {total_mujeres}")
print("-------------------------------")
print(f"Total de Asistentes:              {total_asistentes}")
print(f"Promedio de edad de asistentes:   {promedio_edad:.2f} años")
print(f"Personas rechazadas por edad:     {total_rechazados}")
 
print("\n--- Reporte de Ingresos ---")
# Imprime todos los ingresos por tipo de comprador y el total general.
# Utiliza formato para mostrar dos decimales en el dinero.
print(f"Ingresos por Estudiantes:  ${ingresos_estudiantes:,.2f}")
print(f"Ingresos por Adultos:      ${ingresos_adultos:,.2f}")
print(f"Ingresos por Tercera Edad: ${ingresos_tercera_edad:,.2f}")
print(f"Ingresos por Académicos:   ${ingresos_academicos:,.2f}")
print("-------------------------------")
print(f"TOTAL RECAUDADO: ${ingresos_totales:,.2f}")

print("\n--- Rentabilidad ---")
# --- 7. Mensaje de Rentabilidad ---
# Usa una estructura if/elif/else para determinar si las ganancias
# fueron BAJAS, MODERADAS o BUENAS, basándote en los ingresos totales.
if ingresos_totales < 1500:
    print("La función generó BAJAS ganancias.")
elif ingresos_totales <= 3500:
    print("La función generó ganancias MODERADAS.")
else:
    print("La función generó BUENAS ganancias.")


"""
Preguntas: Explica con tus palabras

1. Imagina que el cine decide implementar una promoción: los martes, todos los boletos de Adulto tendrán un 20% de descuento. 
¿Qué cambios tendrías que hacer en tu código para agregar esta funcionalidad? 
Menciona qué nueva pregunta le harías al usuario y en qué parte del código agregarías la nueva lógica.

Respuesta: Se le consultaría al usuario qué día de la semana nos visita.
Se le pueden asignar números del 1 al 7, empezando con el lunes como día 1
y el domingo como día 7. Este valor se guarda en una variable y, si resulta
igual a 2 (martes) y el tipo de comprador es Adulto, se aplica un descuento
del 20% al precio del boleto. Si no, se cobra con el precio original.

2. Supongamos que, al probar tu programa, el "Total Recaudado en General" siempre te da un resultado incorrecto, 
aunque los ingresos por cada tipo de comprador parecen correctos. 
Describe, paso a paso, qué harías para encontrar el error. 
¿En qué líneas específicas de tu código pondrías atención para verificar los valores y solucionar el problema?

Respuesta: Verificaría los signos de la suma total de lo recaudado y que estén
incluidas todas las variables en la suma, que no estén mal escritas o que no
se esté tomando una variable equivocada con nombre parecido. También revisaría
que dentro de cada elif se estén sumando correctamente los ingresos por tipo
usando +=. Para depurar, agregaría prints temporales después de cada acumulación
con el fin de verificar que los valores cambien correctamente en cada venta.

"""

