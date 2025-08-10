'''

Desarrolla un programa que solicite la carga de un número al usuario.
A continuación, deberá pedir las notas de ese número de alumnos,
y mostrar por pantalla el número de alumnos aprobados y reprobados.

'''

print("Ingrese el numero de alumnos a solicitar")

numero = int(input("Ingrese el numero de alumnos: \n"))

cont_aprobados = 0
cont_reprobados = 0

for x in range(numero) :
    nota = float(input(f"Introduce la nota del alumno {x + 1}: \n"))
    if nota >= 4 :
        cont_aprobados += 1
    else:
        cont_reprobados += 1

print(f"EL numero de aprobados ha sido {cont_aprobados}, y el numero de reprobados {cont_reprobados}")








