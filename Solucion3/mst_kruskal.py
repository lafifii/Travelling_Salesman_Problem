import time
start_time = time.time()

import csv
import math
from collections import namedtuple
from operator import itemgetter 

n = 1500
parent = [0]*n
rango = [0]*n

class edge():
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __lt__(self, otro):
    	return (self.w < otro.w)

def csv2txt(puntos):
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
				puntos.append((x,y))
			if cont>n:
				break
			cont+=1

#	with open('info.txt', 'w') as file:
#		for i in ids:
#			file.write(str(i))
def makeSet(u):
	parent[u] = u
	rango[u] = 0

def findParent(u):
	if(u == parent[u]):
		return u
	parent[u] = findParent(parent[u])
	return parent[u]

def unionset(u,v):
	u = findParent(u)
	v = findParent(v)
	if(u!=v):
		if(rango[u] < rango[v]):
			aux = u
			u = v
			v = aux
		parent[v] = u 
		if(rango[u] == rango[v]):
			rango[u]+=1

def mst(edges, puntos):
	ans = 0
	path = []
	cont = 0
	for i in range (n): 
		makeSet(i)
	for i in range (len(edges)):
		u = edges[i].u
		v = edges[i].v
		w = edges[i].w
		if(findParent(u) != findParent(v)):
			ans+=w
			path.append((u,v))
			unionset(u, v)
	p = []
	for x,y in path:
		p.append((puntos[x][0], puntos[x][1]))
		p.append((puntos[y][0], puntos[y][1]))

	return ans, p

def cal_dis(x1,y1,x2,y2):
	return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def crear(edges, puntos):
	for i in range(n-1):
		for j in range(i+1, n):
			w = cal_dis(puntos[i][0], puntos[i][1],puntos[j][0], puntos[j][1])
			edges.append(edge(i,j,w))

#main
puntos = []
csv2txt(puntos)
edges = []
crear(edges, puntos)
edges.sort()
ans, path= mst(edges, puntos)
print(ans)
print(path)
print("--- %s seconds ---" % (time.time() - start_time))
