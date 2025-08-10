# Muestra un mensaje al usuario para indicar el propósito del programa.
print("Convertidor de C° a K° y F°.")

# Pide al usuario que ingrese la temperatura en grados Celsius.
# La función `input()` lee lo que el usuario escribe como texto (string).
# `int()` convierte ese texto a un número entero (integer), ya que se realizarán cálculos matemáticos.
# El valor ingresado y convertido se guarda en la variable `cgrados`.
cgrados = int(input("Ingrese los C° a convertir: \n"))

# Calcula los grados Kelvin sumando 273 a los grados Celsius.
# El resultado se almacena en la variable `kgrados`.
kgrados = 273 + cgrados

# Calcula los grados Fahrenheit usando la fórmula: (1.8 * C°) + 32.
# El resultado se almacena en la variable `fgrados`.
fgrados = (1.8 * cgrados) + 32

# Imprime un mensaje final mostrando los resultados de las conversiones.
# Se usa un f-string para insertar los valores de las variables `cgrados`, `kgrados` y `fgrados`
# directamente en la cadena de texto, haciéndola fácil de leer.
print(f"Los C° ingresados son: {cgrados}, equivalen a K°: {kgrados}, y a F°: {fgrados}")