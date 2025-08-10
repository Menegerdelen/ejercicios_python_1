# Crea una secuencia de números enteros desde el 1 hasta el 100.
# `range(1, 100 + 1)` genera los números de 1 a 100. El `+ 1` es necesario
# porque la función `range` no incluye el último número.
# Esta secuencia se guarda en la variable `numeros`.
numeros = range(1, 100 + 1)

# Inicia un bucle `for` que itera sobre cada número en la secuencia `numeros`.
# En cada vuelta del bucle, el valor del número actual se asigna a la variable `numero`.
for numero in numeros :
    # Comienza una condición `if` para verificar si el número es par.
    # El operador `%` (módulo) devuelve el residuo de una división.
    # Si `numero % 2 == 0` es verdadero, significa que al dividir el número por 2, el residuo es 0,
    # lo que indica que el número es par.
    if numero % 2 == 0 :
        # Si la condición es verdadera (el número es par), se imprime un mensaje.
        # Se usa un f-string para insertar el valor de la variable `numero` en el mensaje.
        print(f"{numero} es par")