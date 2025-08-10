# Muestra un mensaje en la consola pidiendo al usuario que ingrese tres palabras.
print("Hola, ingrese sus tres palabras: ")

# Muestra un mensaje y espera a que el usuario ingrese la primera palabra.
# El valor ingresado se guarda en la variable 'word1'.
word1 = input("Palabra uno: \n")

# Muestra un mensaje y espera a que el usuario ingrese la segunda palabra.
# El valor ingresado se guarda en la variable 'word2'.
word2 = input("Palabra 2: \n")

# Muestra un mensaje y espera a que el usuario ingrese la tercera palabra.
# El valor ingresado se guarda en la variable 'word3'.
word3 = input("Palabra 3: \n")

# Muestra un mensaje final con las tres palabras que el usuario ingresó.
# Se usa un f-string para insertar el valor de las variables 'word1', 'word2' y 'word3' en la cadena de texto.
print(f"El listado de palabras es: {word1} - {word2} - {word3}")
