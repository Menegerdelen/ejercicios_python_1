# Inicializa una lista vacía llamada `listado`. Aquí se guardarán las alturas ingresadas.
listado = []

# Muestra un mensaje al usuario para explicar el propósito del programa.
print("Lista de alturas")

# Pide al usuario que ingrese la cantidad de personas.
# `input()` lee el valor como texto.
# `int()` lo convierte a un número entero.
# El valor se guarda en la variable `cantidad`.
cantidad = int(input("Cantidad de personas a ingresar: \n"))

# Inicializa un contador para las personas "altas" (altura igual o mayor que el promedio) en 0.
altas = 0

# Inicializa un contador para las personas "bajas" (altura menor que el promedio) en 0.
bajas = 0

# Inicializa una variable `suma` en 0. Se usará para acumular todas las alturas.
suma = 0

# Inicia un bucle `for` que se ejecutará tantas veces como el valor de `cantidad`.
# `range(cantidad)` genera una secuencia de números que controla el número de iteraciones.
for alt in range(cantidad) :
    # Pide al usuario que ingrese la altura de cada persona.
    # `f"..."` se usa para mostrar el número de la persona (empezando en 1).
    # `float()` convierte la entrada a un número decimal.
    altura = float(input(f"Ingrese la altura n° {alt + 1}: \n"))
    
    # Agrega la altura ingresada a la lista `listado` usando el método `.append()`.
    listado.append(altura)

    # Suma la altura actual a la variable `suma`.
    suma += altura

# Calcula el promedio de las alturas.
# Se divide la `suma` total entre la `cantidad` de personas.
# `round(..., 2)` redondea el resultado a 2 decimales para mayor claridad.
promedio = round( suma / cantidad, 2)

# Inicia un segundo bucle `for`, esta vez iterando sobre cada elemento de la lista `listado`.
# La variable `altura` toma el valor de cada elemento de la lista en cada iteración.
for altura in listado :
    # Comienza una estructura `if-else` para comparar cada altura con el promedio.
    # Si la altura es mayor o igual que el promedio, la persona se considera "alta".
    if altura >= promedio :
        # El contador de personas altas (`altas`) se incrementa en 1.
        altas += 1
    # Si la altura es menor que el promedio, la persona se considera "baja".
    else:
        # El contador de personas bajas (`bajas`) se incrementa en 1.
        bajas += 1

# Finalmente, imprime un mensaje con los resultados finales.
# Se usa un f-string para mostrar el promedio, la cantidad de personas altas y la de bajas.
print(f"El promedio de las alturas ingresadas es: {promedio} m. \nLa cantidad de personas altas es: {altas}. \nLa cantidad de personas bajas es: {bajas}")