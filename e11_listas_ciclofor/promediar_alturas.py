

'''
Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float).
Obtener el promedio de las mismas.
Contar cuántas personas son más altas que el promedio y cuántas más bajas.

'''

listado = []

print("Lista de alturas")

cantidad = int(input("Cantidad de personas a ingresar: \n"))

altas = 0
bajas = 0

suma = 0

for alt in range(cantidad) :
    altura = float(input(f"Ingrese la altura n° {alt + 1}: \n"))
    listado.append(altura)

    suma += altura

promedio = round( suma / cantidad, 2)

for altura in listado :
    if altura >= promedio :
        altas += 1
    else:
        bajas += 1



print(f"El promedio de las alturas ingresadas es: {promedio} m. \nLa cantidad de personas altas es: {altas}. \nLa cantidad de personas bajas es: {bajas}")



