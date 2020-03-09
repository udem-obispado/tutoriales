L1 = float(input("Ingresa el primer lado: "))
L2 = float(input("Ingresa el segundo lado: "))
L3 = float(input("Ingresa el tercer lado: "))

if L1 == L2:
    if L2 == L3:
        print(f"El triángulo es equilátero")
    else:
        print(f"El triángulo es isósceles")
else:
    if L2 == L3:
        print(f"El triángulo es isósceles")
    else:
        if L1 == L3:
            print(f"El triángulo es isósceles")
        else:
            print(f"El triángulo es escaleno")