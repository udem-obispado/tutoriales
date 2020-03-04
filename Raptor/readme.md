**Raptor** es un entorno de programación basado en diagramas de flujo, diseñado específicamente para ayudar a los estudiantes a visualizar sus algoritmos y evitar el equipaje sintáctico. Los programas en Raptor se crean visualmente y se ejecutan visualmente al rastrear la ejecución a través del diagrama de flujo. Los estudiantes prefieren usar diagramas de flujo para expresar sus algoritmos, y tienen más éxito creando algoritmos usando Raptor que usando un lenguaje tradicional o escribiendo diagramas de flujo sin Raptor.

![Figura 0-1](images/0-1.png?raw=true)

La interfaz de Raptor contiene 

## 1. PUT (Output)
Output es el símbolo que se utiliza para mostrar en la consola un mensaje específico. El programa de ejemplo **[put-helloworld1.rap](put-helloworld1.rap)** tiene como objetivo mostrar el mensaje "Hello World!" en la consola. Este programa contiene tres símbolos: un _call_ (Clear_Console), un _assignment_ (HW←"Hello World!") y un _output_ (PUT HW).

![Figura 1-1](images/1-1.png?raw=true)

## 2. GET (Input)
Input es el símbolo que se utiliza para generar una ventana para escribir una entrada. Esta entrada se declara como la variable bajo GET. Esta variable cambia con cada prueba de escritorio del programa, lo que la hace independiente del creador del programa y totalmente dependiente al dato ingresado por el usuario. 

El programa de ejemplo **[get-celstofahr1.rap](get-celstofahr1.rap)** tiene como objetivo convertir los grados Celsius ingresados por el usuario a grados Fahrenheit. Este programa contiene cuatro símbolos: el _call_ (Clear_Console), un _input_ (GET C) con el texto "Teclea ºC", un _assignment_ (F←9/5 * C + 32) que es la fórmula de Celsius a Fahrenheit y un _output_ (PUT "Tus grados en  Fahrenheit: "+F).

![Figura 2-1](images/2-1.png?raw=true)

## 3. Funciones
Raptor tiene funciones para realizar operaciones básicas muy útiles. Entre las funciones, las que serán usadas principalmente en los ejercicios son: _e_, _pi_, _random_, _abs(x)_, _ceiling(x)_, _floor(x)_, _sqrt(x)_, _log(x)_, _sin(x)_, _cos(x)_, _tan(x)_, _cot(x)_, _max(x,y)_ y _min(x,y)_.

El programa de ejemplo **[get-maxnum1.rap](get-maxnum1.rap)** tiene como objetivo encontrar el mayor entre dos números. Este programa contiene cinco símbolos: el _call_ (Clear_Console), dos _input_ (GET N1 y GET N2), un _assignment_ (R←max(N1,N2)) que usa la función _max(x,y)_ para encontrar el número mayor de los dos y un _output_ (PUT "De los números "+N1+" y "+N2+" el más grande es "+R+".").

![Figura 3-1](images/3-1.png?raw=true)

## 4. IF (Selection)
Selection es el símbolo que se utiliza para condicionar un resultado de cualquier tipo. Esta condición tiene dos posibles respuestas: sí y no. En pseudocódigo esta estructura se representaría con "Si _tal_ entonces _cual_ Si_no _mal_". Ya que hay solamente dos posibles resultados, se pueden anidar condiciones para expresar más complejidad en los requisitos que se especifican en las condiciones.

### a) oproot

El programa de ejemplo **[if-oproot1.rap](if-oproot1.rap)** tiene como objetivo calcular la raíz cuadrada de un número _si_ este es positivo, _si no_, debe decir que el número es imaginario, ya que la raíz cuadrada de cualquier número negativo es imaginaria. Este programa contiene siete símbolos: el _call_ (Clear_Console), un _input_ (GET REAL) con el texto "Dame un número real", un _selection_ (solicitando que "REAL"<0) que, _si_ se cumple, seguirá un _assignment_ (root←"imaginario") junto con un _output_ (PUT "La raíz cuadrada del número introducido es un número "+root); y que, _si no_ se cumple, seguirá un _assignment_ (root←sqrt(REAL)) junto con un _output_ (PUT "La raíz cuadrada del número introducido es "+root).

![Figura 4-1](images/4-1.png?raw=true)

¿Y si quiero mostrar el resultado de la raíz cuadrada de un número negativo de la forma en que puede ser representado? Los números imaginarios también se pueden denotar escribiendo "i" después de la raíz cuadrada del número y sin el signo negativo. Por eso, el programa de ejemplo **[if-oproot2.rap](if-oproot2.rap)** (que tiene el mismo objetivo que el primer _oproot_) cambia el seguimiento de su condición, por lo que _si "REAL"<0_, entonces seguirá un _assignment_ (coin←sqrt(REAL*-1)) junto con otro _assignment_ (root←(coin)+"i") y un _output_ (PUT "La raíz cuadrada del número introducido es "+root).

![Figura 4-2](images/4-2.png?raw=true)

### b) trgletype

El programa de ejemplo **[if-trgletype1.rap](if-trgletype1.rap)** tiene como objetivo mostrar al usuario de qué tipo es un triángulo en base a la medida de sus lados. Hay tres tipos de triángulos si se clasifican por la medida de los lados (equilátero, isósceles y escaleno). Para poder indicar que un triángulo es de cualquiera de estos tres tipos es imposible usar una sola condición, por lo que deberá tener condiciones anidadas. El programa inicia preguntando al usuario por la medida de cada lado. La primera condición es una igualdad (L1=L2). _Si_ L1=L2 _entonces_ _si_ L2=L3 el triángulo es equilátero y _si no_ el triángulo es isósceles, _si no_ _si_ L2=L3 _entonces_ el triángulo es isósceles y _si no_ _si_ L1=L3 _entonces_ el triángulo es isósceles y _si no_ el triángulo es escaleno.

![Figura 4-3](images/4-3.png?raw=true)

### c) operatns

El programa de ejemplo **[if-operatns1.rap](if-operatns1.rap)** tiene como objetivo calcular la suma, la resta, la multiplicación o la división de dos números que el usuario debe ingresar. El usuario también tiene que elegir cuál de las cuatro operaciones matemáticas realizar. El programa tiene una estructura de condiciones anidadas. Busca primero si el usuario eligió suma, luego resta, después multiplicación y, finalmente, división. Si el usuario no escribe una letra válida, entonces muestra que no se escribió cualquiera de las cuatro letras que pueden escribirse.

![Figura 4-4](images/4-4.png?raw=true)

### d) passgen

El programa de ejemplo **[if-passgen1.rap](if-passgen1.rap)** tiene como objetivo generar una contraseña en base a las respuestas de las preguntas que el programa le hace al usuario.

![Figura 4-6](images/4-6.png?raw=true)

## 5. Operadores
E

## 6. Operadores booleanos
F

## 7. FOR (Loop)
G

## 8. WHILE (Loop)
H

## 9. Funciones booleanas
I

## 10. CALLS (Llamadas)
J

## 11. Subcharts
K

## 12. Procedimientos
L

## 13. RETURN
M

## 14. Unified Modeling Language
N

## 15. Combinación
O
