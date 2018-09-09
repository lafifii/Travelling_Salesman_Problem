# Problema del vendedor viajero

## 1. Introduccion
En el presente documento se presentará el trabajo parcial del curso Complejidad Algorítmica, el cual consiste en **_el problema del vendedor viajero o problema del agente viajero (TSP por sus siglas en inglés)_** , este problema responde a una pregunta ya planteada: dada una lista de ciudades y las distancias entre cada par de ellas, ¿cuál es la ruta más corta posible en la cual el vendedor visita cada ciudad exactamente una vez y al finalizar regresa a la ciudad origen? 

Uno de los principales problemas presentes es la cantidad de datos que se manejarán, el procesamiento y análisis de los mismos ya de por sí es complicado de realizar. Además de realizar un algoritmo óptimo que nos ayude a resolver el problema en un tiempo prudencial.

La principal motivación para la solución de este problema es que este problema presenta diferentes aplicaciones o representaciones en la vida cotidiana, uno de los principales ejemplos el de llegar de la forma más rápida de tu casa a la universidad, al trabajo, etc.

## 2. Objetivos
El presente proyecto tiene los siguientes objetivos:

•	Diseñar un algoritmo que nos permita, a través de una data que fue brindada con anterioridad, organizarla en un archivo .csv para que de esta manera el manejo de la información sea más eficiente, rápido y solo utilizar la información que es relevante para el proyecto.

•	Diseñar un algoritmo que permita mediante la información en el archivo, generar la distancia entre las ciudades.

•	Diseñar un algoritmo que nos permita mediante la distancia entre los puntos, decidir que ruta se debe tomar para lograr el objetivo principal del problema el cual es recorrer todas las ciudades en la distancia mínima.

## 3. Marco teorico
### 3.1. Archivos CSV
Los archivos CSV (del inglés comma-separated values) son un tipo de documento en formato abierto sencillo para representar datos en forma de tabla, en las que las columnas se separan por comas y las filas por saltos de línea.

El formato CSV es muy sencillo y no indica un juego de caracteres concreto, ni cómo van situados los bytes, ni el formato para el salto de línea. Estos puntos deben indicarse muchas veces al abrir el archivo, por ejemplo, con una hoja de cálculo.

El formato CSV no está estandarizado. La idea básica de separar los campos con una coma es muy clara, pero se vuelve complicada cuando los valores del campo también contienen comillas dobles o saltos de línea. Las implementaciones de CSV pueden no manejar esos datos, o usar comillas de otra clase para envolver el campo. Pero esto no resuelve el problema: algunos campos también necesitan embeber estas comillas, así que las implementaciones de CSV pueden incluir caracteres o secuencias de escape.

Además, el término "CSV" también denota otros formatos de valores separados por delimitadores que usan delimitadores diferentes a la coma (como los valores separados por tabuladores). Un delimitador que no está presente en los valores de los campos (como un tabulador) mantiene el formato simple. Estos archivos separados por delimitadores alternativos reciben en algunas ocasiones la extensión, aunque este uso sea incorrecto. Esto puede causar problemas en el intercambio de datos, por ello muchas aplicaciones que usan archivos CSV tienen opciones para cambiar el carácter delimitador.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/CsvDelimited001.svg/113px-CsvDelimited001.svg.png) 
Figura 1. Valores separados por comas.

### 3.2. Exponenciación binaria
La exponenciación binaria es un algoritmo utilizado para calcular de forma rápida grandes potencias enteras de un número x dado. También es conocido como potenciación por cuadrados o elevar al cuadrado y multiplicar. Implícitamente utiliza la expansión binaria del exponente. Es de uso bastante regular en aritmética modular. Este algoritmo es similar al de la duplicación en la multiplicación.

### 3.3. Distancia euclideana
En matemáticas, la distancia euclidiana o euclídea es la distancia "ordinaria" (que se mediría con una regla) entre dos puntos de un espacio euclídeo, la cual se deduce a partir del teorema de Pitágoras.
Por ejemplo, en un espacio bidimensional, la distancia euclidiana entre dos puntos P1 y P2, de coordenadas cartesianas (x1, y1) y (x2, y2) respectivamente, es:
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/92d49b1b717fc1b18de1b7bebddc78d56b9ac79c)
![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Distance_Formula.svg/1024px-Distance_Formula.svg.png)
Figura 2. Distancia en un sistema de coordenadas cartesianas.

### 3.4. Grafos
En matemáticas y ciencias de la computación, un grafo es un conjunto de objetos llamados vértices o nodos unidos por enlaces llamados aristas o arcos, que permiten representar relaciones binarias entre elementos de un conjunto. Son objeto de estudio de la teoría de grafos.

Típicamente, un grafo se representa gráficamente como un conjunto de puntos (vértices o nodos) unidos por líneas (aristas).
Desde un punto de vista práctico, los grafos permiten estudiar las interrelaciones entre unidades que interactúan unas con otras. Por ejemplo, una red de computadoras puede representarse y estudiarse mediante un grafo, en el cual los vértices representan terminales y las aristas representan conexiones (las cuales, a su vez, pueden ser cables o conexiones inalámbricas).
Prácticamente cualquier problema puede representarse mediante un grafo, y su estudio trasciende a las diversas áreas de las ciencias exactas y las ciencias sociales.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/6n-graf.svg/333px-6n-graf.svg.png)
Figura 3. Grafo etiquetado con 6 vértices y 7 aristas.

### 3.5. Algoritmo del vecino más cercano
El algoritmo del vecino más próximo fue, en las ciencias de la computación, uno de los primeros algoritmos utilizados para determinar una solución para el problema del viajante. Este método genera rápidamente un camino corto, pero generalmente no el ideal.

Abajo está la aplicación del algoritmo del vecino más próximo al problema del viajante.
Estos son los pasos del algoritmo:
1.	elección de un vértice arbitrario respecto al vértice actual.
2.	descubra la arista de menor peso que ya esté conectada al vértice actual y a un vértice no visitado V.
3.	convierta el vértice actual en V.
4.	marque V como visitado.
5.	si todos los vértices del dominio estuvieran visitados, cierre el algoritmo.
6.	vaya al paso 2.

La secuencia de los vértices visitados es la salida del algoritmo.
El algoritmo del vecino más próximo es fácil de implementar y ejecutar rápidamente, pero algunas veces puede perder rutas más cortas, que son fácilmente notadas con la visión humana, debido a su naturaleza más "ávida". Como norma general, si los últimos pasos del recorrido son comparables en longitud al de los primeros pasos, el recorrido es razonable; si estos son mucho mayores, entonces es probable que existan caminos mucho mejores.

![](https://matediscretasjoaquin.webnode.es/_files/200000009-70ef771e88/EJEM.jpg)
Figura 4. Grafo inicial

![](https://matediscretasjoaquin.webnode.es/_files/200000012-6e3806f317/ejem4.jpg)
Figura 5. Grafo final solucionado con el vecino más cercano

### 3.6. Algoritmo de los K vecinos más cercanos
El método de los k vecinos más cercanos (en inglés, k-nearest neighbors, abreviado k-nn) es un método de clasificación supervisada (Aprendizaje, estimación basada en un conjunto de entrenamiento y prototipos) que sirve para estimar la función de densidad F (x / C j) de las predictoras x por cada clase C j.

Este es un método de clasificación no paramétrico, que estima el valor de la función de densidad de probabilidad o directamente la probabilidad a posteriori de que un elemento x pertenezca a la clase C j a partir de la información proporcionada por el conjunto de prototipos. En el proceso de aprendizaje no se hace ninguna suposición acerca de la distribución de las variables predictoras.

En el reconocimiento de patrones, el algoritmo k-nn es usado como método de clasificación de objetos (elementos) basado en un entrenamiento mediante ejemplos cercanos en el espacio de los elementos. k-nn es un tipo de aprendizaje vago (lazy learning), donde la función se aproxima solo localmente y todo el cómputo es diferido a la clasificación.

Regla K-NN
----------

Al aplicar la regla NN, se explora todo el conocimiento almacenado en el conjunto de entrenamiento para determinar cuál será la clase a la que pertenece una nueva muestra, pero únicamente tiene en cuenta el vecino más próximo a ella, por lo que es lógico pensar que es posible que no se esté aprovechando de forma eficiente toda la información que se podría extraer del conjunto de entrenamiento.

Con el objetivo de resolver esta posible deficiencia surge la regla de los k vecinos más cercanos (k-NN). La regla k-NN es una extensión de la regla NN, en la que se utiliza la información suministrada por los k prototipos del conjunto de entrenamiento más cercanos de una nueva muestra para su clasificación.

Formalmente se define la vecindad de los k vecinos más cercanos de una muestra x como:

Sea un conjunto de entrenamiento de N prototipos pertenecientes a M clases distintas, E el Reconocimiento de patrones espacio de representación de los objetos y x una muestra (). Se define como vecindad al conjunto de prototipos del conjunto de entrenamiento que cumple las tres condiciones siguientes:

La expresión anterior significa que la regla k-NN determina que la clase a la cual pertenece una nueva muestra x es la más votada por sus k vecinos más cercanos.

![](https://www.ecured.cu/images/5/59/K_NN.JPG)

Figura 6. Regla de los K vecinos más cercanos

Ejemplo de funcionamiento
-------------------------
En la imagen superior se ilustra el funcionamiento de esta regla de clasificación. En ella se encuentran representadas 12 muestras pertenecientes a dos clases distintas: la Clase 1 está formada por 6 cuadrados de color azul y la Clase 2 formada por 6 círculos de color rojo. En este ejemplo, se han seleccionado tres vecinos, es decir, (k=3).

De los 3 vecinos más cercanos a la muestra x, representada en la figura por una cruz, uno de ellos pertenece a la Clase 1 y los otros dos a la Clase 2. Por tanto, la regla 3-NN asignará la muestra x a la Clase 2. Es importante señalar que si se hubiese utilizado como regla de clasificación la NN, la muestra x sería asignada a la Clase 1, pues el vecino más cercano de la muestra x pertenece a la Clase 1. 
## 4. Conclusiones
