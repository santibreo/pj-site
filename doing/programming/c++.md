# Curso C++

## Módulo 1

### Graph theory
C++ is a better C. Creado por los desarrolladores de UNIX. El prototipo previo fue SIL (System Implementation Language).

C++ fue creado por Stroustrup, 13 años más tarde con 63 palabras clave (C tenía 29), soporte para programación imperativa, orientada a objetos y genérica. Su creador procedía de una tradición de programación orientada a objetos y traslado sus conocimientos a C, en lo que en un primer momento se llamo _C con clases_. Este lenguaje evolucionó hasta soportar también otros tipos de programación. C++ tiene más características que C y es más simple, luego por eso decimos que es esencialmente mejor.

Si comparamos con Java, Java es más puramente orientado a objetos, y tiene las JVM mientras que C++ se compila directamente a C. Por lo tanto suele ser el lenguaje de alto nivel que mejor se compila. Para la comunidad de programadores podríamos decir que están parejos.

### Getting started
Object Orientations no es sobre el control de flujo pero exige que te sientas cómodo con la recursividad. Un objeto es un tipo de dato y sus operaciones pueden definirse de forma nativa o por el propio usuario. OOP permite la extensión de tipos, de forma que una vez se genera una clase esta puede llevar asociado un tipo. Podemos decir así que la característica esencial de la programación orientada a objetos es la extensión de tipos.

### Converting a C Programm
Codigo asociado al cálculo de _odds_ en un juego de dados:
```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIDES 6
#define R_SIDE (rand() % SIDES +1)
void main()
{
	srand(clock());
	printf("\nEnter number of trials:");
	scanf("%d", &trials);
	for(j=0; j<trials; ++j)
		outcomes[(d1 = R_SIDE) + (d2 = R_SIDE)]++;
	printf("probability\n")
	for(j=2; j<n_dice*SIDES +1: ++j)
		printf("j = %d    p = %lf\n", j, (double)(outcomes[j])/trials);
	return 0;
}
```
Todos los comandos/macros _(#cosas)_ son lo que llamamos comandos de preprocesado, y en __C++__ trataremos de no usarlos más. El uso del reloj como _seed_ de los números aleatorios es una forma de evitar el comportamiento determinista de nuestro ordenador. 

### Using C++ Code & C++ improvements $ C++ advantages
Ahora el código de nuestro programa en __C++__ quedaría:
```cpp
//The following program computes the probability for dice possibilities
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
const int sides = 6: //replaces de defines statements
inline int r_sides(){return(rand() % sides +1);}

int main(void)
{
	const int n_dice = 2;
	int d1, d2;
	srand(clock())
	cout<< "\nEnter number of trials: ";
	int trials;
	cin>> trials;
	int* outcomes = new int[n_dice * sides +1]
	for(int j=0; j<trials; ++j)
		outcomes[(d1 = r_sides()) + (d2 = r_sides())]++;
	cout<< "probability\n"
	for(int j=2; j<n_dice*sides +1: ++j)
		cout << "j = " << j << " p = "
			 << static_cast<double>(outcomes[j]/trials
			 << endl;
	return 0;
}
```
Un _namespace_ es un contexto, podemos cargar distintos contextos e incluso mezclarlos. _inline_ es una nueva palabra clave, es un _compiler directive_ que nos permite evitar llamadas al compilador. Vemos además aparecer __<<__ que es lo que se llama _overloaded_ y lo que hace es cargar en el prompt lo que venga después.

Bjarne Stroustrup: _"I don't think 'purity' is a virtue. The signal strngth of C++ is exactly that it supports several effective styles of programming (several paradigms, if you must), and combinations of these styles. Often, the most elegant, most efficient, and the most maintainable solution involves more than one style (paradigm)."_

### C++ is better than C
+ More type safe: int, char, double, int* (pointer type), etc
+ More libraries
+ Less reliance on preprocesoor
+ OO vs imperative

C fue diseñado para ser compilado en una arquitectura local, y que esa compilación estuviera altamente optimizada.  

### C Swap Function & Swap Function in C++
Podemos ver:
```c
void swap(int* i, int* j){
	int temp = *i;
	*i = *j;
	*j = temp;
}
void swap_double(double* i, double* j){
	double temp = *i;
	*i = *j;
	*j = temp;
}

// To call swap we must use
swap(&par1, &par2)
```

Pointers consumen direcciones, es decir, no les importa el contenido grabado en 
esa dirección si no los bits alojados allí, contengan lo que contengan.  El 
símbolo `*` al principio indica _dereference_ que significa que estamos mirando 
a la dirección representada por la variable. Así en la tercera línea el 
contenido de la dirección j se está moviendo a la i. La segunda función está 
para demostrar que necesitamos otra función, con prácticamente el mismo código, 
para hacer lo mismo, con parámetros de un tipo distinto.

Ahora en C++ podemos verlo también:
```cpp
#include <iostream>
using namespace std;
inline void swap(int& i, int& j){
	int temp = i;
	i = j;
	j = temp;
}
inline void swap(double& i, double& j){
	double temp = i;
	i = j;
	j = temp;
}
```
IO significa type safe y es conveniente e intuitivo. Inline para hacer el código más eficiente que llamando al compilador. C++ tiene _overloading_ lo que significa que podemos alojar dos funciones en el mismo contexto coon el mismo nombre, en función de los tipos de los argumentos el compilador llamará a una o a la otra. De esta forma el _overloading_ implica distinción por el tipo y el número de argumentos que se pasen a la función. Más adelante veremos `cpp template` que es una opción incluso más poderosa.

`cpp cout` y `cpp <<` _(bit shift operator)_ se encuentran en la librería __*iostream*__. `cpp inline` se emplea para declarar funciones de una forma más rápida, pero evita llamar al compilador, luego solo debe usarse con funciones cortas.

### Generics

En la programación en C++, _generics_ hace referencia al uso de templates. Los templates son para evitar la reescritura de código que es esencialmente muy similar (como una receta) pero con ligeras variaciones (ingredientes distintos).
```cpp
#include <iostream>
using namespace std;
template <class T>
inline void swap(T& i, T& j){
	T temp = i;
	i = j;
	j = temp;
}
```

template es una nueva palabra clave, lo que viene detrás de class es un identificador, que se suele marcar en mayúsculas por convención. Lo llamamos metavariable y va a ser sustituido por un tipo de dato. Añadiendo esa línea ya tendríamos una función `cpp swap` universal. La sustitución de `cpp T` por el tipo de dato la hace el compilador automáticamente al encontrar algo que coincide con `cpp T`.

Ejemplo de template para una función que suma los elementos de un vector:
```cpp
//The following program computes the probability for dice possibilities
#include <iostream>
using namespace std;
template <class SUM>
inline void sum(const SUM data[], int size, SUM s=0){
	for(int i=0; i < size; i++)
		s += data[i];
	return s
}
```

## Módulo 2

_Enum types_ fueron creados para ser un tipo simple que permitiera generar un pequeño conjunto de constantes con nombres asignados como un tipo. Al principio era un tipo integral:
```cpp
enum Answers{Yes, No, Maybe}; // Yes = 0, No = 1. Maybe = 2
```

Que también podían no tener nombre, o ser asignadas explícitamente, de forma que enteros específicos eran empleados como enumeradores. 
```cpp
enum {FahrenheitBoiling = 100, CelsiusBoiling = 212} 
```

Ocurría que valores enteros específicos podían ser ambiguos, al estar definidos para varios enumeradores. Por ello se introdujo la clase _enum_.
```cpp
enum class Permission{Yes, No};
enum class AnswerClass{Yes, No, Maybe};
```

Para el caso de los enumeradores planos, estos eran convertidos a enteros automáticamente, sin embargo, al ser una clase esto dejó de ser así. 
```cpp
int i = Answers::Yes //Ningún problema
int j = AnswerClass::Yes //Error
int j = static_cast<int>(AnswerClass::Yes) //Es lo necesario ahora
```

Podemos especificar el tipo de entero subyacente mediante dos puntos.

```cpp
enum class CarType:short{Sedan, Coupe, SUV, Convertible}
```

Admitiéndose `cpp char, short, int, long, longlong` y sus formas sin signo. 

_Ira Pohl supplementary example on overloading operator:_
```cpp
#include<iostream>
#include<cstdint>
using namespace std;
enum class days:std::int8_t{
	SUNDAY,MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY
};
//unlike plain enums C++11 enum class is typesafe and does not silently
//convert to int
ostream& operator<<(ostream& out, const days& d){
	out << static_cast<int>(d); return out;
}
days operator++(days& d){ //PREFIX OPERATOR
	d = static_cast<days>((static_cast<int>(d) + 1) % 7); return d;
}
days operator++(days& d, int){ //POSTFIX OPERATOR
	days temp = d;
 	d = static_cast<days>((static_cast<int>(d) + 1) % 7);
 	return temp;
}
int main(){
 	days today{days::MONDAY};
 	std::cout << "Demonstrate class enum" << std::endl;
 	std::cout << "MONDAY VALUE IS " << today << std::endl;
 	std::cout << "INCREMENT VALUE IS " << ++today << std::endl;
 	std::cout << "INCREMENT VALUE IS " << today++ << std::endl;
 	std::cout << "INCREMENT VALUE IS " << today << std::endl;
 	return 0;
}
```



```cpp

```

```cpp

```

```cpp

```

```cpp

```

```cpp

```

```cpp

```
