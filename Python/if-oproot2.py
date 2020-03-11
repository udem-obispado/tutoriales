import math
# Esto importará las funciones matemáticas

REAL = float(input("Dame un número real: "))
# "float(x)" dejará que el número tenga decimales
# "input(x)" generará un cuadro de entrada

if REAL < 0:
    coin = round(math.sqrt((REAL*(-1))), 2)
    root = str(coin)+"i"
    print(f"La raíz cuadrada del número introducido es {root}")
    # Los números imaginarios también se pueden denotar escribiendo "i" después de la raíz cuadrada del número sin el signo negativo
    # "print" imprimirá el texto o resultado
else:
    root = math.sqrt(REAL)
    print(f"La raíz cuadrada del número introducido es {round(root, 2)}")
    # "math.sqrt(x)" sacará la raíz cuadrada del número
    
