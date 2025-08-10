'''

Desarrolla un programa que solicite constantemente la carga de un número al usuario.
El programa finalizará cuando el usuario introduzca un 0, momento en el que se debe visualizar
la suma y el promedio de todos los números introducidos.

'''

print("Ingrese numeros para sumar y promediar, si desea terminar ingrese 0: \n")

suma = 0
numero = -1
contador = 0

while numero != 0 :
    numero = int(input("Ingrese numero: \n"))
    if numero != 0 :
        suma += numero
        contador += 1

promedio = round(suma / contador, 2)

print(f"La suma de todos los numeros es {suma}, y su promedio es {promedio}")
