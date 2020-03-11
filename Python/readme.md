**Python** es un lenguaje de programación interpretado, dinámico y multiplataforma, el cual se enfoca en la legibilidad de su código. Es multiparadigma, ya que soporta orientación a objetos, programación imperativa y programación funcional. Python posee una filosofía que se compone de 19 principios, escritos por Tim Peters en _El Zen de Python_. Las aplicaciones más útiles para crear programas en Python son Jupyter, Python IDLE y Visual Studio Code.

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
Python tiene funciones para realizar operaciones básicas muy útiles. Las funciones también son conocidas como métodos o procedimientos. Entre las funciones, las que serán usadas principalmente en los ejercicios son: _e_, _pi_, _float(x)_, _ceil(x)_, _floor(x)_, _str(x)_, _ord(x)_, _hex(x)_, _oct(x)_, _sqrt(x)_, _len(x)_, _chr(x)_, _unichr(x)_, _dict(d)_, _tuple(s)_, _list(s)_, _max(x,y)_, _min(x,y)_, _int(x [,base])_, _long(x [,base])_, _round(x [,dec])_ y _complex(real [,imag])_.

El programa de ejemplo **[input-celstofahr1.py](input-celstofahr1.py)** tiene como objetivo convertir los grados Celsius ingresados por el usuario a grados Fahrenheit. Utiliza la función _float(x)_ para que Python interprete la entrada como un número decimal y la función _round(x [,dec])_ para que el número tenga una cantidad de cifras decimales especificada.

![Figura 3-1](images/3-2.png?raw=true)

## 4. If Else Elif
If es la función que se utiliza para condicionar un resultado de cualquier tipo. Esta condición tiene dos posibles respuestas: sí y no. En pseudocódigo esta estructura se representaría con "Si _tal_ entonces _cual_ Si_no _mal_". Ya que hay solamente dos posibles resultados, se pueden anidar condiciones para expresar más complejidad en los requisitos que se especifican.

### a) oproot

El programa de ejemplo **[if-oproot1.py](if-oproot1.py)** tiene como objetivo calcular la raíz cuadrada de un número _si_ este es positivo, _si no_, debe decir que el número es imaginario, ya que la raíz cuadrada de cualquier número negativo es imaginaria.

![Figura 4-1](images/4-1.png?raw=true)

¿Y si quiero mostrar el resultado de la raíz cuadrada de un número negativo de la forma en que puede ser representado? Los números imaginarios también se pueden denotar escribiendo "i" después de la raíz cuadrada del número y sin el signo negativo. Por eso, el programa de ejemplo **[if-oproot2.py](if-oproot2.py)** (que tiene el mismo objetivo que el primer _oproot_) cambia el seguimiento de su condición para que el número imaginario pueda ser mostrado.

![Figura 4-2](images/4-2.png?raw=true)

### b) trgletype

El programa de ejemplo **[if-trgletype1.py](if-trgletype1.py)** tiene como objetivo mostrar al usuario de qué tipo es un triángulo en base a la medida de sus lados. Hay tres tipos de triángulos si se clasifican por la medida de los lados (equilátero, isósceles y escaleno). Para poder indicar que un triángulo es de cualquiera de estos tres tipos es imposible usar una sola condición, por lo que deberá tener condiciones anidadas. El programa inicia preguntando al usuario por la medida de cada lado. La primera condición es una igualdad (L1=L2). _Si_ L1=L2 _entonces_ _si_ L2=L3 el triángulo es equilátero y _si no_ el triángulo es isósceles, _si no_ _si_ L2=L3 _entonces_ el triángulo es isósceles y _si no_ _si_ L1=L3 _entonces_ el triángulo es isósceles y _si no_ el triángulo es escaleno.

![Figura 4-3](images/4-3.png?raw=true)

### c) operatns

### d) passgen

## 5. Return

## 6. Creación de funciones
Además de las funciones que vienen integradas en Python, existe la posibilidad de crear funciones propias. Esto es posible escribiendo "def", con el nombre de la función y paréntesis ().
