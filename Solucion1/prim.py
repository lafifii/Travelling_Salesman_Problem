import time
start_time = time.time()

import csv
import math
from collections import namedtuple
from operator import itemgetter 

n = 2000

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

def mst(graph, puntos, s):
	ans = 0
	oo = 100000009
	dis = [oo]*n
	used = [False]*n
	dis[s] = 0
	path = []
	for it in range(n):
		u = -1
		dismin = oo
		for i in range(n):
			if(not used[i] and dis[i] < dismin):
				dismin = dis[i]
				u = i

		if(u==-1):
			break
		used[u] = True
		path.append(u)
		ans+=dis[u]

		for i in range(len(graph[u])):
			v = graph[u][i]
			w = cost[u][i]
			if(not used[v] and dis[v]):
				dis[v] = w

	return ans, path

def cal_dis(x1,y1,x2,y2):
	return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def crear(graph, puntos, cost):
	for i in range(n-1):
		for j in range(i+1, n):
			w = cal_dis(puntos[i][0], puntos[i][1],puntos[j][0], puntos[j][1])
			graph[i].append(j)
			graph[j].append(i)
			cost[i].append(w)
			cost[j].append(w)

#main
puntos = []
csv2txt(puntos)
graph = [0]*n
cost = [0]*n
for i in range(n):
	graph[i] = []
	cost[i] = []

crear(graph, puntos, cost)
ans, path = mst(graph, puntos, 0)
print(ans)
print(path)

print("--- %s seconds ---" % (time.time() - start_time))
