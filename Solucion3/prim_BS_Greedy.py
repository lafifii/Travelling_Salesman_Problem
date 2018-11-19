import time
start_time = time.time()

import csv
import random
import math
import json
from collections import namedtuple
from operator import itemgetter 

n =  100000
lad = [None]*n
cost = [None]*n
for i in range(n):
	lad[i] = []
	cost[i] = []

def csv2txt(puntos):
	global n
	ids = []
	with open('IE_P.csv') as file:
		reader = csv.reader(file)
		cont = 0
		for fila in reader:
			if cont != 0:
				alo = str(cont) +"," + fila[3] + "\n"
				ids.append(alo)
				x = int(float(fila[5])*100)
				y = int(float(fila[6])*100)
				idx = fila[3]
				puntos.append([x,y, idx])
			if cont>n:
				break
			cont+=1

def cal_dis(x1,y1,x2,y2):
	return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def crear(puntos):
	for i in range(n-1):
		for j in range(i+1, n):
			w = cal_dis(puntos[i][0], puntos[i][1],puntos[j][0], puntos[j][1])
			lad[i].append(j)
			cost[i].append(w)
			lad[j].append(i)
			cost[j].append(w)

def prim(src, path):
	global n
	ans = 0
	dis = [1e9]*n
	used = [False]*n
	dis[src] = 0
	for it in range(n):
		u = -1
		dismin = 1e9
		for i in range(n):
			if(not used[i] and dis[i] < dismin):
				dismin = dis[i]
				u = i
		if(u==-1):break
		used[u] = True
		path.append(u)
		ans+=dis[u]

		for i in range(len(lad[u])):
			v = lad[u][i]
			w = cost[u][i]
			if(not used[v] and w < dis[v]):
				dis[v] = w

	return ans

def pot(num,b):
	if(b==0):
		return 1
	x = pot(n,b/2)
	x = x*x 
	if(b%2 == 0):
		return x
	else:
		return x*n
def bs(ar, x):
	lo = 0
	hi = len(ar) - 1
	while(lo < hi):
		med = int((lo+hi)/2)
		if(ar[med] == x):
			return x
		elif(x < ar[med]):
			hi = med - 1
		else:
			lo = med + 1

	return -1

def aleatorio(PA):
	global n
	ans = 0
	random.shuffle(PA)
	for i in range(n-1):
		ind = bs(lad[PA[i]], PA[i+1])
		ans+=cost[PA[i]][ind]

	return ans	

def pathcoordenadas(coordenadas_en_orden_del_path, path, puntos):
    for i in range(len(path)):
        coordenadas_en_orden_del_path.append(puntos[path[i]])

def createLinks(p):
    mn = len(p)
    ret = [{"source": p[mn-1], "target": p[0]}]
    for i in range(1,mn):
        ret.append({"source": p[i], "target": p[i-1]})
    return ret

def createNodes(d):
    ret = []
    for x, y , idx in d:
        ret.append({"x": x, "y": y, "cod": idx})
    return ret

def crearLugar(distancias):
    ret = []
    for i in distancias:
        ret.append( { "X": i[0], "Y": i[1], "PROV": i[2]} )
    return ret

#main
puntos = []
csv2txt(puntos)
crear(puntos)
path = []
PA = []
for i in range(n):
	PA.append(i)

ans = prim(0, path)
#iteraciones = int(math.pow(10, 5 - int(math.log10(n))))
#for i in range(iteraciones): #O(it)*(n)*log(n)
#	disaux = aleatorio(PA)
#	if(disaux < ans):
#		ans = disaux
#		path = PA

print(ans)
coordenadas_en_orden_del_path  = []

for i in range(len(path)):
	coordenadas_en_orden_del_path.append(puntos[path[i]])

nd = createNodes(coordenadas_en_orden_del_path)
lk = createLinks(path)
data = {"nodes": nd, "links": lk}

with open('graphIEP_1678.json', 'w') as outfile:
    json.dump(data, outfile)

pt = []
for i in path:
    pt.append(i)
fpt = [{"node": pt}]
with open('pathIEP_1678.json', 'w') as outfile:
    json.dump(fpt, outfile)

lg = crearLugar(puntos)
data = {"lugar": lg}
with open('info.json', 'w') as outfile:
    json.dump(data, outfile)

print("--- %s seconds ---" % (time.time() - start_time))
