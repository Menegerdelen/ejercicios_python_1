# Muestra un mensaje de bienvenida para que el usuario sepa qué hacer.
print("Hola estudiante, ingrese sus notas a continuacion")

# Pide al usuario que ingrese la primera nota.
# `input()` lee el valor como texto.
# `float()` lo convierte a un número decimal, que es lo más adecuado para notas.
# El valor se guarda en la variable `nota1`.
nota1 = float(input("Nota 1: \n"))

# Repite el proceso para la segunda nota y la guarda en `nota2`.
nota2 = float(input("Nota 2: \n"))

# Repite el proceso para la tercera nota y la guarda en `nota3`.
nota3 = float(input("Nota 3: \n"))

# Calcula el promedio de las notas.
# ¡Ojo! En este código hay un pequeño error: está sumando `nota3` dos veces. La línea correcta debería ser:
# `promedio = (nota1 + nota2 + nota3) / 3`
# El resultado del cálculo se guarda en la variable `promedio`.
promedio = (nota3 + nota2 + nota3) / 3

# Inicia una estructura de control `if-else` para tomar una decisión.
# Comprueba si el valor de `promedio` es mayor o igual a 4.
if promedio >= 4 :
    # Si la condición es verdadera (el promedio es 4 o más), imprime "PROMOCIONADO".
    print("PROMOCIONADO")
else:
    # Si la condición es falsa (el promedio es menor que 4), imprime "NO PROMOCIONADO".
    print("NO PROMOCIONADO")