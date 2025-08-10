'''
Desarrolla una calculadora de enteros
El programa deberá pedir los dos operandos al usuario y realizar las operaciones básicas:
- Suma
- Resta
- Multiplicación
- División
También se debe controlar las excepciones que se puedan producir

'''
print("Calculadora")

try :
    num1 = int(input("Ingrese el primer numero: \n"))
    num2 = int(input("Ingrese el segundo numero: \n"))
except :
    print("Los numeros ingresados no son validos. Se establecera valores por defectp a los numeros solicitados")
    num1 = 10
    num2 = 2

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

try :
    division = round(num1 / num2, 2)
except :
    print("Error de division")
    division = "ERROR"

print(f"La suma de {num1} + {num2} es {suma}")
print(f"La resta de {num1} - {num2} es {resta}")
print(f"La multiplicacion de {num1} x {num2} es {multiplicacion}")
print(f"La division de {num1} : {num2} es {division}")

