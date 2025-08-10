# Se muestra un mensaje para que el usuario sepa qué debe ingresar.
print("Hola, ingrese el area del circulo para calcular su radio.")

# Se le pide al usuario que ingrese el valor del radio.
# La función `input()` recibe el valor como texto.
# La función `float()` lo convierte a un número decimal para poder hacer cálculos.
# El valor final se guarda en la variable `radio`.
radio = float(input("Ingrese el area del circulo: \n"))

# Se define una variable `pi` y se le asigna un valor aproximado de 3.14.
pi = 3.14

# Se calcula el área del círculo usando la fórmula: pi * radio al cuadrado (pow(radio, 2)).
# La función `round()` redondea el resultado a 2 decimales para que sea más legible.
# El resultado se guarda en la variable `area`.
area = round(pi * pow(radio, 2),2)

# Se muestra el resultado final al usuario.
# Se utiliza un f-string para insertar los valores de las variables `radio` y `area`
# directamente dentro de la cadena de texto.
print(f"El area del circulo de radio: {radio}, es {area}")


