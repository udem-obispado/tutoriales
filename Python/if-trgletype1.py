L1 = float(input("Ingresa el primer lado: "))
L2 = float(input("Ingresa el segundo lado: "))
L3 = float(input("Ingresa el tercer lado: "))

if L1 == L2:
    if L2 == L3:
        print(f"El triángulo es equilátero")
        # "print" imprimirá el texto o resultado
    else:
        print(f"El triángulo es isósceles")
        # "print" imprimirá el texto o resultado
else:
    if L2 == L3:
        print(f"El triángulo es isósceles")
        # "print" imprimirá el texto o resultado
    else:
        if L1 == L3:
            print(f"El triángulo es isósceles")
            # "print" imprimirá el texto o resultado
        else:
            print(f"El triángulo es escaleno")
            # "print" imprimirá el texto o resultado
