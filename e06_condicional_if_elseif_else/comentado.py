# Muestra un mensaje al usuario explicando el propósito del programa.
print("Revise si tiene aumento de sueldo, ingresando su sueldo actual y su años de antiguedad")

# Pide al usuario que ingrese su sueldo actual.
# `input()` lee el valor como texto.
# `int()` convierte ese texto a un número entero para poder hacer cálculos.
# El valor se guarda en la variable `sueldo`.
sueldo = int(input("Ingrese su sueldo: \n"))

# Pide al usuario que ingrese los años de antigüedad y lo guarda en la variable `anos`.
anos = int(input("Ingrese sus años de antiguedad: \n"))

# Calcula el aumento del 20% y lo guarda en `aumento1`.
# La fórmula es `sueldo * 0.2` para el 20% del sueldo, que luego se suma al sueldo original.
aumento1 = (sueldo * 0.2) + sueldo

# Calcula el aumento del 5% y lo guarda en `aumento2`.
# La fórmula es `sueldo * 0.05` para el 5% del sueldo, que luego se suma al sueldo original.
aumento2 = (sueldo * 0.05) + sueldo

# Inicia la primera estructura de control `if-elif-else` para decidir qué mensaje mostrar.
# La condición verifica si el sueldo es menor a 500 Y los años de antigüedad son 10 o más.
if 500 > sueldo and anos >= 10 :
    # Si se cumple la condición, muestra un mensaje con el nuevo sueldo calculado.
    print(f"Se le ha otorgado un aumento del 20%, su nuevo sueldo es: {aumento1}")

# La siguiente condición se evalúa si la anterior es falsa.
# Verifica si el sueldo es menor a 500 Y los años de antigüedad son menos de 10.
elif 500 > sueldo and 10 > anos :
    # Si se cumple esta condición, muestra un mensaje con el nuevo sueldo del 5%.
    print(f"Se le ha otorgado un aumento del 5%, su nuevo sueldo es: {aumento2}")

# Si ninguna de las condiciones anteriores se cumple, se ejecuta el bloque `else`.
else:
    # Muestra un mensaje indicando que no hay aumento.
    print(f"Su sueldo es: {sueldo}")

# Inicia la segunda estructura `if-elif` para modificar el valor real de la variable `sueldo`.
# Esta estructura es casi idéntica a la anterior, pero en lugar de imprimir, actualiza el valor de `sueldo`.
# Se verifica si el sueldo es menor a 500 Y los años son 10 o más.
if 500 > sueldo and anos >= 10 :
    # Si es verdadero, el sueldo se actualiza sumándole el 20% de su valor.
    # El `+=` es una forma abreviada de `sueldo = sueldo + (0.2 * sueldo)`.
    sueldo += 0.2 * sueldo

# Si la condición anterior es falsa, se verifica si el sueldo es menor a 500 Y los años son menos de 10.
elif 500 > sueldo and 10 > anos :
    # Si es verdadero, el sueldo se actualiza sumándole el 5% de su valor.
    sueldo += 0.05 * sueldo

# Finalmente, imprime el valor del sueldo después de las posibles modificaciones.
# Esta línea se ejecuta sin importar si hubo aumento o no, mostrando el sueldo final.
print(f"El sueldo final es: {sueldo}")