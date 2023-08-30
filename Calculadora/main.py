from operaciones import suma, multiplicacion, resta, division


x = int(input("Inserte el primer numero: "))

y = int(input("Inserte el segundo numero: "))


print("La suma es: ", suma(x, y))
print("La resta es: ", resta(x, y))
print("La multiplicacion es: ", multiplicacion(x, y))
try:
    print("La division es: ", division(x, y))
except ZeroDivisionError:
    print("No se puede dividir entre 0")
