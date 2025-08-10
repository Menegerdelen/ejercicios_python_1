'''
De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea dichos datos del teclado y realice lo siguiente:
- Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %.
- Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.
- Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.

'''
print("Revise si tiene aumento de sueldo, ingresando su sueldo actual y su años de antiguedad")

sueldo = int(input("Ingrese su sueldo: \n"))
anos = int(input("Ingrese sus años de antiguedad: \n"))

aumento1 = (sueldo * 0.2) + sueldo
aumento2 = (sueldo * 0.05) + sueldo

if 500 > sueldo and anos >= 10 :
    print(f"Se le ha otorgado un aumento del 20%, su nuevo sueldo es: {aumento1}")
elif 500 > sueldo and 10 > anos :
    print(f"Se le ha otorgado un aumento del 5%, su nuevo sueldo es: {aumento2}")
else:
    print(f"Su sueldo es: {sueldo}")

if 500 > sueldo and anos >= 10 :
    sueldo += 0.2 * sueldo
elif 500 > sueldo and 10 > anos :
    sueldo += 0.05 * sueldo

print(f"El sueldo final es: {sueldo}")







