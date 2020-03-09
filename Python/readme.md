**Python** es un lenguaje de programación interpretado, dinámico y multiplataforma, el cual se enfoca en la legibilidad de su código. Es multiparadigma, ya que soporta orientación a objetos, programación imperativa y programación funcional. Python tiene una filosofía, que se compone de 19 principios escritos por Tim Peters en _El Zen de Python_. Las aplicaciones más útiles para crear programas en Python son Jupyter, Python IDLE y Visual Studio Code.

![Figura 0-1](images/0-1.png?raw=true)

En Jupyter, para ejecutar una celda de código, simplemente debe ser clicado el menú "Run" y luego el botón "Run Selected Cell". Su respectivo atajo en el teclado es "Shift"+"Enter". En el lado izquierdo de la ventana aparece todo el directorio de archivos del sistema.

## 1. Print (Output)
Print es la función que se utiliza para mostrar en la consola un mensaje específico. El programa de ejemplo **[print-helloworld1.py](print-helloworld1.py)** tiene como objetivo mostrar el mensaje "Hello World!" en la consola. Primero se declaró la variable HW, que en el programa será "Hello World!", con lo que luego se imprimirá el valor de HW.

![Figura 1-1](images/1-2.png?raw=true)

## 2. Input
Input es la función que se utiliza para generar un cuadro para introducir texto, que se volverá el valor de la variable. Esta variable cambia con cada prueba de escritorio del programa, lo que la hace independiente del creador del programa y totalmente dependiente al dato ingresado por el usuario.

El programa de ejemplo **[input-name1.py](input-name1.py)** tiene como objetivo mostrar el nombre de una persona al ingresarlo el usuario. Entonces, _print("¿Cuál es tu nombre?")_ imprimirá la pregunta, _nombre = input()_ asignará la entrada como "nombre" y _print(f"Buenos días, {nombre}")_ mostrará el texto "Buenos días" junto con el valor de "nombre".

![Figura 2-1](images/2-2.png?raw=true)

## 3. Funciones
Raptor tiene funciones para realizar operaciones básicas muy útiles. Entre las funciones, las que serán usadas principalmente en los ejercicios son: _float(x)_, _str(x)_, _repr(x)_, _ord(x)_, _hex(x)_, _oct(x)_, _chr(x)_, _unichr(x)_, _dict(d)_, _tuple(s)_, _list(s)_, _set(s)_, _eval(str)_, _int(x [,base])_, _long(x [,base])_, _round(x [,dec])_ y _complex(real [,imag])_.

El programa de ejemplo **[input-celstofahr1.py](input-celstofahr1.py)** tiene como objetivo convertir los grados Celsius ingresados por el usuario a grados Fahrenheit. Utiliza la función _float(x)_ para que Python interprete la entrada como un número decimal y la función _round(x [,dec])_ para que el número tenga una cantidad de cifras decimales especificada.

![Figura 3-1](images/3-2.png?raw=true)
