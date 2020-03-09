import math

REAL = float(input("Dame un número real: "))

if REAL < 0:
    root = "imaginario"
    print(f"La raíz cuadrada del número introducido es un número {root}")
else:
    root = math.sqrt(REAL)
    print(f"La raíz cuadrada del número introducido es {round(root, 2)}")