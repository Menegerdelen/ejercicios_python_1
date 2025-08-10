# Escribe un programa que pida al usuario el radio de un círculo y calcule su área, sabiendo que: Área = pi r^2

print("Hola, ingrese el area del circulo para calcular su radio.")

radio = float(input("Ingrese el area del circulo: \n"))
pi = 3.14
area = round(pi * pow(radio, 2),2)

print(f"El area del circulo de radio: {radio}, es {area}")
