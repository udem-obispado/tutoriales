import math
# Esto importará las funciones matemáticas

REAL = float(input("Dame un número real: "))
# float(x) dejará que el número tenga decimales

if REAL < 0:
    root = "imaginario"
    print(f"La raíz cuadrada del número introducido es un número {root}")
    # root se debe especificar en 
else:
    root = math.sqrt(REAL)
    print(f"La raíz cuadrada del número introducido es {round(root, 2)}")
