N1 = float(input("Ingresa el primer número: "))
N2 = float(input("Ingresa el segundo número: "))
OP = input("Escribe S para sumar, R para restar, M para multiplicar o D para dividir")

if OP == "S":
    RS = N1+N2
    print(f"La suma de los dos números es: {RS}")
elif OP == "R":
    RS = N1-N2
    print(f"La resta de los dos números es: {RS}")
elif OP == "M":
    RS = N1*N2
    print(f"El producto de los dos números es: {RS}")
elif OP == "D":
    RS = N1/N2
    print(f"El cociente de los dos números es: {RS}")
else:
    print("La letra que has ingresado no es válida. S para sumar, R para restar, M para multiplicar o D para dividir")
    