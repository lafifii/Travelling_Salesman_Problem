import csv
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial as spatial

def csv2txt(distancias):
	ids = []
	with open('informacion.csv') as file:
		reader = csv.reader(file)
		cont = 0
		for fila in reader:
			if cont != 0:
				alo = str(cont) +"," + fila[3] + "\n"
				ids.append(alo)
				x = float(fila[15])
				y = float(fila[16])
				distancias.append((x,y))
			if cont>150000:
				break
			cont+=1

	with open('info.txt', 'w') as file:
		for i in ids:
			file.write(str(i))

"""forma mas eficiente de hacer potencia -f"""
def potenciacionBinaria(base,exponente):
	if exponente:
		return 1
	x = potenciacionBinaria(base,exponente>>2)
	x = x*x
	if b%2 == 0:
		return x
	else:
		return x*n

def euclideanDistance(a,b):
	distance = potenciacionBinaria(a[0] - b[0],2) + potenciacionBinaria(a[1] - b[1],2)
	return math.sqrt(distance)

def createGraph(grafo,distancias):
	
	n = len(distancias)
	print(n)
	for i in range(n):
		disV = set([])
		for j in range(i+1,100):
			ds = euclideanDistance(distancias[i], distancias[j])
			disV.add((ds,j))
			print(disV)

def nearest_neighbors(points, k):
	point_tree = spatial.cKDTree(points)
	cmap = plt.get_cmap('copper')
	colors = cmap(np.linspace(0, 1, len(points)))

	for center, group, color  in zip(points, point_tree.query_ball_point(points, 0.5), colors):
	   cluster = point_tree.data[group]
	   x, y = cluster[:, 0], cluster[:, 1]
	   plt.scatter(x, y, c=color, s=200)

	plt.show()

def make_pairs(ind,dist,k,grafo,i):
	arrpairs = []
	for i in range(k+1):
		arrpairs.append((ind[i], dist[i]))
	print(arrpairs)


def knn(distancias,grafo,n):
	tree = spatial.cKDTree(distancias)   

	for i in range(n):        
		dist, ind = tree.query(distancias[i], k=3)
		make_pairs(ind,dist,k,grafo,i)

def printLAD(grafo,n):
	for i in range(n):
		for elem in grafo[i]:
			print(elem, end="  ")
		print("")
distancias = []
k = 2
csv2txt(distancias)
distancias = np.array(distancias)
n = len(distancias)

grafo = [[] for i in range(n)]
knn(distancias,grafo,n)