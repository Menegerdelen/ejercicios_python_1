# Muestra un mensaje de bienvenida para indicar el propósito del programa.
print("Calculadora")

# Inicia un bloque `try`, que intenta ejecutar un código que podría generar un error.
try :
    # Pide al usuario que ingrese el primer número.
    # `input()` lee el valor como texto.
    # `int()` intenta convertir el texto a un número entero. Si no puede, causará un error.
    num1 = int(input("Ingrese el primer numero: \n"))

    # Pide al usuario que ingrese el segundo número y lo convierte a entero.
    num2 = int(input("Ingrese el segundo numero: \n"))

# El bloque `except` se ejecuta si ocurre un error dentro del bloque `try`.
# En este caso, si el usuario ingresa algo que no es un número, se ejecuta este código.
except :
    # Muestra un mensaje de error.
    print("Los numeros ingresados no son validos. Se establecera valores por defecto a los numeros solicitados")
    # Asigna valores por defecto (10 y 2) a las variables para que el programa continúe.
    num1 = 10
    num2 = 2

# Realiza las operaciones matemáticas básicas con los números.
# Suma de `num1` y `num2`.
suma = num1 + num2
# Resta de `num1` y `num2`.
resta = num1 - num2
# Multiplicación de `num1` y `num2`.
multiplicacion = num1 * num2

# Inicia otro bloque `try` para manejar la división, que puede causar un error si el divisor es cero.
try :
    # Intenta realizar la división.
    # `round(num1 / num2, 2)` calcula la división y redondea el resultado a 2 decimales.
    division = round(num1 / num2, 2)

# Si ocurre un error (por ejemplo, al dividir por cero), se ejecuta este bloque `except`.
except :
    # Muestra un mensaje de error específico para la división.
    print("Error de division")
    # Asigna la cadena de texto "ERROR" a la variable `division`.
    division = "ERROR"

# Imprime los resultados de las operaciones.
# Se usan f-strings para mostrar los valores de las variables de forma clara en cada línea.
print(f"La suma de {num1} + {num2} es {suma}")
print(f"La resta de {num1} - {num2} es {resta}")
print(f"La multiplicacion de {num1} x {num2} es {multiplicacion}")
print(f"La division de {num1} : {num2} es {division}")