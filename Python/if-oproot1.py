import math
# Esto importará las funciones matemáticas

REAL = float(input("Dame un número real: "))
# "float(x)" dejará que el número tenga decimales
# "input(x)" generará un cuadro de entrada

if REAL < 0:
    root = "imaginario"
    print(f"La raíz cuadrada del número introducido es un número {root}")
    # "print" imprimirá el texto o resultado
else:
    root = math.sqrt(REAL)
    print(f"La raíz cuadrada del número introducido es {round(root, 2)}")
    # "math.sqrt(x)" sacará la raíz cuadrada del número
