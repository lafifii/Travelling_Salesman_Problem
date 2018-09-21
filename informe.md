# Problema del vendedor viajero

## 1. Introduccion
En el presente documento se presentará el trabajo parcial del curso Complejidad Algorítmica, el cual consiste en **_el problema del vendedor viajero o problema del agente viajero (TSP por sus siglas en inglés)_** , este problema responde a una pregunta ya planteada: dada una lista de ciudades y las distancias entre cada par de ellas, ¿cuál es la ruta más corta posible en la cual el vendedor visita cada ciudad exactamente una vez y al finalizar regresa a la ciudad origen? 

Uno de los principales problemas presentes es la cantidad de datos que se manejarán, el procesamiento y análisis de los mismos ya de por sí es complicado de realizar. Además de realizar un algoritmo óptimo que nos ayude a resolver el problema en un tiempo prudencial.

La principal motivación para la solución de este problema es que este problema presenta diferentes aplicaciones o representaciones en la vida cotidiana, uno de los principales ejemplos el de llegar de la forma más rápida de tu casa a la universidad, al trabajo, etc.

## 2. Objetivos
El presente proyecto tiene los siguientes objetivos:

•Diseñar un algoritmo que nos permita, a través de una data que fue brindada con anterioridad, organizarla en un archivo .csv para que de esta manera el manejo de la información sea más eficiente, rápido y solo utilizar la información que es relevante para el proyecto.

•Diseñar un algoritmo que permita mediante la información en el archivo, generar la distancia entre las ciudades.

•Diseñar un algoritmo que nos permita mediante la distancia entre los puntos, decidir que ruta se debe tomar para lograr el objetivo principal del problema el cual es recorrer todas las ciudades en la distancia mínima.

## 3. Marco teorico
### 3.1. Archivos CSV
Los archivos CSV (del inglés comma-separated values) son un tipo de documento en formato abierto sencillo para representar datos en forma de tabla, en las que las columnas se separan por comas y las filas por saltos de línea.

El formato CSV es muy sencillo y no indica un juego de caracteres concreto, ni cómo van situados los bytes, ni el formato para el salto de línea. Estos puntos deben indicarse muchas veces al abrir el archivo, por ejemplo, con una hoja de cálculo.

El formato CSV no está estandarizado. La idea básica de separar los campos con una coma es muy clara, pero se vuelve complicada cuando los valores del campo también contienen comillas dobles o saltos de línea. Las implementaciones de CSV pueden no manejar esos datos, o usar comillas de otra clase para envolver el campo. Pero esto no resuelve el problema: algunos campos también necesitan embeber estas comillas, así que las implementaciones de CSV pueden incluir caracteres o secuencias de escape.

Además, el término "CSV" también denota otros formatos de valores separados por delimitadores que usan delimitadores diferentes a la coma (como los valores separados por tabuladores). Un delimitador que no está presente en los valores de los campos (como un tabulador) mantiene el formato simple. Estos archivos separados por delimitadores alternativos reciben en algunas ocasiones la extensión, aunque este uso sea incorrecto. Esto puede causar problemas en el intercambio de datos, por ello muchas aplicaciones que usan archivos CSV tienen opciones para cambiar el carácter delimitador.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/CsvDelimited001.svg/113px-CsvDelimited001.svg.png) 
Figura 1. Valores separados por comas.

### 3.2. Distancia euclideana
En matemáticas, la distancia euclidiana o euclídea es la distancia "ordinaria" (que se mediría con una regla) entre dos puntos de un espacio euclídeo, la cual se deduce a partir del teorema de Pitágoras.
Por ejemplo, en un espacio bidimensional, la distancia euclidiana entre dos puntos P1 y P2, de coordenadas cartesianas (x1, y1) y (x2, y2) respectivamente, es:
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/92d49b1b717fc1b18de1b7bebddc78d56b9ac79c)
![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Distance_Formula.svg/1024px-Distance_Formula.svg.png)
Figura 2. Distancia en un sistema de coordenadas cartesianas.

### 3.3. Grafos
En matemáticas y ciencias de la computación, un grafo es un conjunto de objetos llamados vértices o nodos unidos por enlaces llamados aristas o arcos, que permiten representar relaciones binarias entre elementos de un conjunto. Son objeto de estudio de la teoría de grafos.

Típicamente, un grafo se representa gráficamente como un conjunto de puntos (vértices o nodos) unidos por líneas (aristas).
Desde un punto de vista práctico, los grafos permiten estudiar las interrelaciones entre unidades que interactúan unas con otras. Por ejemplo, una red de computadoras puede representarse y estudiarse mediante un grafo, en el cual los vértices representan terminales y las aristas representan conexiones (las cuales, a su vez, pueden ser cables o conexiones inalámbricas).
Prácticamente cualquier problema puede representarse mediante un grafo, y su estudio trasciende a las diversas áreas de las ciencias exactas y las ciencias sociales.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/6n-graf.svg/333px-6n-graf.svg.png)
Figura 3. Grafo etiquetado con 6 vértices y 7 aristas.

### 3.4. Algoritmo del vecino más cercano
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

### 3.5. Algoritmo de los K vecinos más cercanos
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

## 4.Solución del problema TSP
### 4.1.Por algoritmo Greedy
```python

if "xrange" not in globals():
    xrange = range
else:
    pass

def optimize_solution( distances, connections, endpoints ):
    N = len(connections)
    path = restore_path( connections, endpoints )
    def ds(i,j): 
        pi = path[i]
        pj = path[j]
        if pi < pj:
            return distances[pj][pi]
        else:
            return distances[pi][pj]
            
    d_total = 0.0
    optimizations = 0
    for a in xrange(N-1):
        b = a+1
        for c in xrange( b+2, N-1):
            d = c+1
            delta_d = ds(a,b)+ds(c,d) -( ds(a,c)+ds(b,d))
            if delta_d > 0:
                d_total += delta_d
                optimizations += 1
                connections[path[a]].remove(path[b])
                connections[path[a]].append(path[c])
                connections[path[b]].remove(path[a])
                connections[path[b]].append(path[d])

                connections[path[c]].remove(path[d])
                connections[path[c]].append(path[a])
                connections[path[d]].remove(path[c])
                connections[path[d]].append(path[b])
                path[:] = restore_path( connections, endpoints )
    
    return optimizations, d_total
        
def restore_path( connections, endpoints ):
    if endpoints is None:
        start, end = [idx 
                      for idx, conn in enumerate(connections)
                      if len(conn)==1 ]
    else:
        start, end = endpoints

    path = [start]
    prev_point = None
    cur_point = start
    while True:
        next_points = [pnt for pnt in connections[cur_point] 
                       if pnt != prev_point ]
        if not next_points: break
        next_point = next_points[0]
        path.append(next_point)
        prev_point, cur_point = cur_point, next_point
    return path

def _assert_triangular(distances):
    for i, row in enumerate(distances):
        if len(row) < i: 
        	return
    

def pairs_by_dist(N, distances):
    indices = []
    for i in xrange(N):
        for j in xrange(i):
            indices.append(i*N+j)

    indices.sort(key = lambda ij: distances[ij//N][ij%N])
    return ((ij//N,ij%N) for ij in indices)

def solve_tsp( distances, optim_steps=3, pairs_by_dist=pairs_by_dist, endpoints=None ):
    N = len(distances)
    if N == 0: return []
    if N == 1: return [0]

    _assert_triangular(distances)
    node_valency = pyarray('i', [2])*N 
    if endpoints is not None:
        start, end = endpoints
        if start == end: raise ValueError("start=end is not supported")
        node_valency[start]=1
        node_valency[end]=1
        
    connections = [[] for i in xrange(N)] 

    def join_segments(sorted_pairs):
        segments = [ [i] for i in xrange(N) ]
  
        def possible_edges():
            for ij in sorted_pairs:
                i,j = ij
                if node_valency[i] and node_valency[j] and\
                   (segments[i] is not segments[j]): 
                    yield ij
                    
        def connect_vertices(i,j):
            node_valency[i] -= 1
            node_valency[j] -= 1
            connections[i].append(j)
            connections[j].append(i)
            seg_i = segments[i]
            seg_j = segments[j]
            if len(seg_j) > len(seg_i):
                seg_i, seg_j = seg_j, seg_i
                i, j = j, i
            for node_idx in seg_j:
                segments[node_idx] = seg_i
            seg_i.extend(seg_j)
            
        def edge_connects_endpoint_segments(i,j):
            si,sj = segments[i],segments[j]
            ss,se = segments[start], segments[end]
            return (si is ss) and (sj is se) or (sj is ss) and (si is se)
               
        edges_left = N-1
        for i,j in possible_edges():
            if endpoints and edges_left!=1 and edge_connects_endpoint_segments(i,j):
                continue #para que no terimne antes de lo que debe
           
            connect_vertices(i,j)
            edges_left -= 1
            if edges_left == 0:
                break

    join_segments(pairs_by_dist(N, distances))
    for passn in range(optim_steps):
        nopt, dtotal = optimize_solution( distances, connections, endpoints )
        if nopt == 0:
            break
return restore_path( connections, endpoints=endpoints )

n = 1500

def csv2txt(distancias):
	ids = []
	with open('informacion.csv') as file:
		reader = csv.reader(file)
		cont = 0
		for fila in reader:
			if cont != 0:
				alo = str(cont) +"," + fila[3] + "\n"
				ids.append(alo)
				x = int(float(fila[15])*100)
				y = int(float(fila[16])*100)
				distancias.append((x,y))
			if cont>n:
				break
			cont+=1

	with open('info.txt', 'w') as file:
		for i in ids:
			file.write(str(i))

def cal_dis(x1,y1,x2,y2):
	return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

distancias = []
D = []
for i in range(n):
	aux = []
	for j in range(n):
		aux.append(0)
	D.append(aux)

csv2txt(distancias)

for i in range(n):
	disxvertice = []
	for j in range(n):
		x1 = distancias[i][0]
		y1 = distancias[i][1]
		x2 = distancias[j][0]
		y2 = distancias[j][1]
		disxvertice.append((cal_dis(x1,y1,x2,x2) , j))

	sorted(disxvertice)

	for kk in range(3):
		dis_aux = disxvertice[i][0]
		des_aux = disxvertice[i][1]
		D[i][des_aux] = D[des_aux][i] = dis_aux

path = solve_tsp( D )
print(path)
```
### Análisis de complejidad del Algoritmo Greedy:
Para cada punto, debes encontrar al vecino más cercano. (obtienes la primera n)
Calcular la distancia entre dos puntos obtienes un factor 1, porque se ejecuta en O (1).
Calcular la distancia entre un punto y todos los demás puntos te da un factor O (n).
En total obtienes O (n²). Por más que no debas calcular la distancia a los puntos visitados pero esto no resta complejidad. ya que es O(1)
Para el vecino más cercano de un punto A es el punto más cercano a A. Entonces debes calcular n puntos. La distancia a todos los otros puntos, así que se obtiene también O (n²)

Sumar esto resulta en O (n² + n²) = O (2n²) = O (n²)

### 4.2. Por programación dinámica con Bitmasking
```python
INT_MAX  = 999999
n=20
dist = [[0 for x in range(140)] for y in range(140)]
todos_vis = (1<<n) -1;
dp = [[0 for x in range(20)] for y in range(1048576)]

def csv2txt(distancias):
	global n
	ids = []
	with open('informacion.csv') as file:
		reader = csv.reader(file)
		cont = 0
		for fila in reader:
			if cont != 0:
				alo = str(cont) +"," + fila[3] + "\n"
				ids.append(alo)
				x = int(float(fila[15])*100)
				y = int(float(fila[16])*100)
				distancias.append((x,y))
			if cont>n:
				break
			cont+=1

	with open('info.txt', 'w') as file:
		for i in ids:
			file.write(str(i))

def cal_dis(x1,y1,x2,y2):
	return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def tsp(mask,pos): 
	global dp,INT_MAX,todos_vis
	if(mask==todos_vis):
		return dist[pos][0]
	if(dp[mask][pos]!=-1):
	   return dp[mask][pos]
	ans = INT_MAX;
	for ciudad in range(n):
		if((mask&(1<<ciudad))==0):
			ans2 = dist[pos][ciudad] + tsp( mask|(1<<ciudad), ciudad);
			ans = min(ans, ans2);

	dp[mask][pos] = ans
	return dp[mask][pos];

#main
distancias = []
csv2txt(distancias)
for i in range(n):
	for j in range(n):
		dist[i][j] = cal_dis(distancias[i][0],distancias[j][0],distancias[i][1],distancias[j][1]) 

for i in range(1<<n): #2 a la n
	for j in range(n):
		dp[i][j] = -1;

print("tsp dp + bitmasking ", tsp(1,0))
```
### Análisis de complejidad programación dinámica por Bitmasking:

Considerando el número de nodos como n. Entonces, hay n*(2^n) estados y cada estado se esta iterando sobre los n nodos para poder llegar al siguiente estado y para cuestiones de memoria, esta transición de iteraciones se hacen una sola vez por cada estado.
Entonces el tiempo de complejidad es representado por: O (n * (n*(2^n)) = O (n^2 * 2^n)

### 4.3. Por Backtracking:
```python
n = 10
posibles_ans = []
configuraciones = [0]*n

def csv2txt(distancias):
	global n
	ids = []
	with open('informacion.csv') as file:
		reader = csv.reader(file)
		cont = 0
		for fila in reader:
			if cont != 0:
				alo = str(cont) +"," + fila[3] + "\n"
				ids.append(alo)
				x = int(float(fila[15])*100)
				y = int(float(fila[16])*100)
				distancias.append((x,y))
			if cont>n:
				break
			cont+=1

	with open('info.txt', 'w') as file:
		for i in ids:
			file.write(str(i))

def cal_dis(x1,y1,x2,y2):
	return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def verificar(distancias):
	suma = 0
	for i in range(n-1):
		i1 = configuraciones[i]
		i2 = configuraciones[i+1]
		suma = suma + cal_dis(distancias[i1][0],distancias[i2][0],distancias[i1][1],distancias[i2][1])
	posibles_ans.append(suma)
	
def tsp(pos, distancias): 
	if(pos==n-1):
		verificar(distancias)
		return
	for i in range(1,n+1):
		configuraciones[pos] = i
		tsp(pos+1, distancias)
		configuraciones[pos] = -1

#main
distancias = []
csv2txt(distancias)
configuraciones[0] = configuraciones[n-1] = 0 #empieza en ciudad indexada 0
tsp(0, distancias)
sorted(posibles_ans)
print("bt <-> brute force", posibles_ans[0]) #la menor suma
```
### Análisis de complejidad por Backtracking:
Se tiene n+1 espacios que llenar en las configuraciones y en cada uno podemos poner n numeros indexados 0 - n-1  tenemos un tiempo promedio de O(n!) además de ello para cada configuración queremos guardar la distancia que se recorrio con esa haciendo suma de todas las distancias que es una complejidad n.
Al final se tiene : O (n! * n)

## 5. Conclusiones
Las conclusiones del proyecto son las siguientes:

•La generación y uso de los archivos .csv nos permiten y facilitan la gestión y almacenamiento de datos, además de tenerla de forma más ordenada y con fácil acceso a través del Python.

•El problema del TSP, el cual nos indica que debemos recorrer toda una trama de puntos en la distancia más corta, nos ayuda a entender mejor y comprender problemas cotidianos, en los cuales debemos tener en cuenta los recursos, distancia, tiempo y dinero que se invertirán para llegar de un lugar a otro.

•El uso de un algoritmo Greedy, aunque no siempre es el más óptimo, nos ayuda a obtener una solución rasonable y en su medida medianamente óptima un problema, adicionalmente que su complejidad es O (n²), a diferencia de otros como el fuerza bruta que posee complejidad O(n!).

•El uso de la programación dinámica, es un razonamiento inductivo muy potente en la resolución de problemas, aplicable a problemas de optimización, en este caso el TSP.

•El uso del backtracking nos permite resolver diversos tipos de problemas, pero a su vez, este requiere de mucha memoria, debido a el gran espacio de búsqueda que normalmente adopta.
