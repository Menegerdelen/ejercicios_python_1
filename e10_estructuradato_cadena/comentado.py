# Muestra un mensaje al usuario explicando el propósito del programa.
print("Calcular espacios en blanco")

# Pide al usuario que ingrese una oración.
# La función `input()` lee toda la línea de texto que el usuario escribe.
# El texto se guarda en la variable `oracion`.
oracion = input("Ingrese su oracion: \n")

# Usa el método `.count()` para contar cuántas veces aparece un carácter específico
# (en este caso, un espacio en blanco " ") dentro de la cadena de texto `oracion`.
# El resultado del conteo se almacena en la variable `espacios`.
espacios = oracion.count(" ")

# Imprime el resultado final.
# Se usa un f-string para insertar el valor de la variable `espacios` en el mensaje.
print(f"La cantidad de espacios en blanco en la oracion es: {espacios}")