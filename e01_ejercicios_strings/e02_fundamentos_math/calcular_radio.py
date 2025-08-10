# Escribe un programa que pida al usuario el radio de un círculo y calcule su área, sabiendo que: Área = pi r^2

print("Hola, , ahora calcule el radio del circulo")

radio = float(input("Ingrese el area del circulo: \n"))
pi = 3.14
area = round(pi * pow(radio, 2),2)

print(f"El area del circulo de {radio}, es {area}")
