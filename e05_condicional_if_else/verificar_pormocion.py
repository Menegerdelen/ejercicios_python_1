# Escribir un programa que pida las tres notas de un alumno. Si el promedio es mayor o igual a 4, mostrar un mensaje "Promocionado".


print("Hola estudiante, ingrese sus notas a continuacion")

nota1 = float(input("Nota 1: \n"))
nota2 = float(input("Nota 2: \n"))
nota3 = float(input("Nota 3: \n"))

promedio = (nota3 + nota2 + nota3) / 3

if promedio >= 4 :
    print("PROMOCIONADO")
else:
    print("NO PROMOCIONADO")



