# Muestra un mensaje al usuario explicando el propósito del programa y cómo terminarlo.
print("Ingrese numeros para sumar y promediar, si desea terminar ingrese 0: \n")

# Inicializa la variable `suma` en 0. Esta variable acumulará la suma de todos los números ingresados.
suma = 0

# Inicializa la variable `numero` en -1. Esto asegura que el bucle `while` se ejecute al menos una vez,
# ya que la condición del bucle es `numero != 0`.
numero = -1

# Inicializa el contador de números en 0. Esto servirá para calcular el promedio.
contador = 0

# Comienza un bucle `while` que continuará ejecutándose mientras la variable `numero` no sea igual a 0.
while numero != 0 :
    # Pide al usuario que ingrese un número.
    # `input()` lee el valor como texto.
    # `int()` lo convierte a un número entero.
    # El valor se guarda en la variable `numero`.
    numero = int(input("Ingrese numero: \n"))
    
    # Comienza una condición `if` para verificar si el número ingresado no es 0.
    # Esto evita que el 0 se sume y se cuente.
    if numero != 0 :
        # Si el número no es 0, se añade a la variable `suma`.
        # `+=` es una forma abreviada de `suma = suma + numero`.
        suma += numero
        # También se incrementa el contador de números en 1.
        contador += 1

# Una vez que el bucle `while` termina (el usuario ingresó 0), se calcula el promedio.
# Se divide la `suma` total por el `contador` de números ingresados.
# `round(..., 2)` redondea el resultado a 2 decimales para que sea más legible.
# El resultado se guarda en la variable `promedio`.
promedio = round(suma / contador, 2)

# Finalmente, se imprime un mensaje que muestra la suma total y el promedio calculado.
# Se usa un f-string para insertar los valores de `suma` y `promedio` en el texto.
print(f"La suma de todos los numeros es {suma}, y su promedio es {promedio}")

