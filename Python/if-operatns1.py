N1 = float(input("Ingresa el primer número: "))
N2 = float(input("Ingresa el segundo número: "))
OP = input("Escribe S para sumar, R para restar, M para multiplicar o D para dividir")

if OP == "S":
    RS = N1+N2
    print(f"La suma de los dos números es: {RS}")
elif OP == "R":
    RS = N1-N2
    print(f"La resta de los dos números es: {RS}")
    # elif se usa para anidar una condición en la condición principal.
elif OP == "M":
    RS = N1*N2
    print(f"El producto de los dos números es: {RS}")
    # elif se usa para anidar una condición en la condición principal.
elif OP == "D":
    RS = N1/N2
    print(f"El cociente de los dos números es: {RS}")
    # elif se usa para anidar una condición en la condición principal.
else:
    print("La letra que has ingresado no es válida. Te sugiero que escribas S para sumar, R para restar, M para multiplicar o D para dividir")
