import math

REAL = float(input("Dame un número real: "))

if REAL < 0:
    coin = round(math.sqrt((REAL*(-1))), 2)
    root = str(coin)+"i"
    print(f"La raíz cuadrada del número introducido es un número {root}")
else:
    root = math.sqrt(REAL)
    print(f"La raíz cuadrada del número introducido es {round(root, 2)}")