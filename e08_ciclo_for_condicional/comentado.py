# Muestra un mensaje al usuario para que sepa qué información se le pedirá.
print("Ingrese el numero de alumnos a solicitar")

# Solicita al usuario el número total de alumnos.
# `input()` lee la entrada como texto.
# `int()` convierte el texto en un número entero, que es necesario para el bucle.
# El valor se guarda en la variable `numero`.
numero = int(input("Ingrese el numero de alumnos: \n"))

# Inicializa un contador para los alumnos aprobados en 0.
cont_aprobados = 0

# Inicializa un contador para los alumnos reprobados en 0.
cont_reprobados = 0

# Inicia un bucle `for` que se repetirá tantas veces como el valor de la variable `numero`.
# `range(numero)` crea una secuencia de números desde 0 hasta `numero - 1`.
# En cada iteración, la variable `x` toma el siguiente valor de la secuencia.
for x in range(numero) :
    # Dentro del bucle, se pide la nota para cada alumno.
    # `input()` lee la nota como texto.
    # `float()` la convierte a un número decimal (para notas como 4.5, etc.).
    # `x + 1` se usa para mostrar el número de alumno de forma más amigable (empezando por 1 en lugar de 0).
    nota = float(input(f"Introduce la nota del alumno {x + 1}: \n"))
    
    # Comienza una estructura `if-else` para clasificar la nota.
    # Si la nota es 4 o superior, el alumno está "aprobado".
    if nota >= 4 :
        # Si se cumple la condición, el contador de aprobados (`cont_aprobados`) aumenta en 1.
        # `+= 1` es una forma corta de decir `cont_aprobados = cont_aprobados + 1`.
        cont_aprobados += 1
    # Si la nota es menor que 4, el alumno está "reprobado".
    else:
        # Si no se cumple la condición, el contador de reprobados (`cont_reprobados`) aumenta en 1.
        cont_reprobados += 1

# Una vez que el bucle ha terminado (se han revisado todos los alumnos), se imprime el resultado.
# Se usa un f-string para mostrar el número total de aprobados y reprobados.
print(f"EL numero de aprobados ha sido {cont_aprobados}, y el numero de reprobados {cont_reprobados}")