'''
Escribe un programa que pida al usuario los grados centígrados que quiere convertir,
y muestre por pantalla la equivalencia con grados kelvin y grados fahrenheit.

Fórmulas:
- ºK = 273 + ºC
- ºF = 1.8 × ºC + 32

'''

print("Convertidor de C° a K° y F°.")

cgrados = int(input("Ingrese los C° a convertir: \n"))
kgrados =  273 + cgrados
fgrados = (1.8 * cgrados) + 32

print(f"Los C° ingresados son: {cgrados}, equivalen a K°: {kgrados}, y a F°: {fgrados}")

