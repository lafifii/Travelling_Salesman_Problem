import math
import csv

n = 15000
visitado = [False]*n
# Al usar un algoritmo greedy estamos buscando la solucion mas optima para cada caso con la
# esperanza de que el resultado final sea el más optimo tambien. Es asi que empezamos en 
# un nodo, en este caso la ciudad 0 y vemos cual es el más cercano, luego estaremos
# en aquella ciudad y realizamos el mismo procedimiento hasta haber visitado todas las 
# ciudades. Esta solucion no sera la mas optima en un problema NP de ninguna manera
# mas es la que puede aguantar mayor cantidad de datos en un tiempo razonable
# la complejidad es O(n^2) y su uso de memoria no es demasiado grande 
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

def solve_tsp(distancias):
	path = [0]
	suma = 0
	prev = 0 #Ultimo nodo visitado
	visitado[prev] = True
	while(len(path) < n):
		#Seguiremos hasta haber pasado por todas las ciudades
		distancias_desdePunto = [] #Primero distancia y 2 vertice

		for i in range(n):
			if(i == prev):
				continue
			if(visitado[i] == True):
				continue
			
			x1 = distancias[i][0]  
			y1 = distancias[i][1]
			x2 = distancias[prev][0]
			y2 = distancias[prev][1]
			dis = cal_dis(x1,y1,x2,y1)
			distancias_desdePunto.append((dis, i))

		distancias_desdePunto.sort(key=lambda tup: tup[0]) 
		path.append(distancias_desdePunto[0][1]) #Camino
		prev = distancias_desdePunto[0][1] #Actual nodo
		visitado[prev] = True
		suma = suma + distancias_desdePunto[0][0] #Suma de distancias

	return suma, path
def pathcoordenadas(coordenadas_en_orden_del_path, path, distancias):
	for i in range(len(path)):
		coordenadas_en_orden_del_path.append(distancias[path[i]])

distancias = []
csv2txt(distancias)
suma, path = solve_tsp(distancias)
coordenadas_en_orden_del_path = []
pathcoordenadas(coordenadas_en_orden_del_path, path, distancias)
print(path)
print("Distancia recorrida ", suma)
print(coordenadas_en_orden_del_path)
