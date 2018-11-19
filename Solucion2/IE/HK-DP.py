import time
start_time = time.time()

import itertools
import random
import json
import sys
import csv
import math
from collections import namedtuple
from operator import itemgetter 

n = 17
#O(n^2 * 2^n) Complejidad ,  2^n * n Espacio.
def csv2txt(puntos):
	global n
	ids = []
	with open('IE_P.csv') as file:
		reader = csv.reader(file)
		cont = 0
		for f in reader:
			if cont != 0:
				x = int(float(f[5])*100)
				y = int(float(f[6])*100)
				CODLOCAL = f[0]
				CEN_EDU = f[1]
				CODCPSIG = f[2]
				NOMCPSIG = f[3]
				puntos.append([x,y,CODLOCAL, CEN_EDU, CODCPSIG, NOMCPSIG])
			if cont>n:
				break
			cont+=1

def HK(dists):
    global n
    C = {}
    for k in range(1, n):
        C[(1 << k, k)] = (dists[0][k], 0)
    for _ in range(2, n):
        for subs in itertools.combinations(range(1, n), _):
            bits = 0
            for bit in subs:
                bits |= 1 << bit
            for k in subs:
                prev = bits & ~(1 << k)
                res = []
                for m in subs:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dists[m][k], m))
                C[(bits, k)] = min(res)
    bits = (2**n - 1) - 1
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + dists[k][0], k))
    opt, parent = min(res)
    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits

    path.append(0)

    return opt, list(reversed(path))

def cal_dis(x1,y1,x2,y2):
	return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def crear(dists, puntos):
	for i in range(n):
		for j in range(n):
			valor = cal_dis(puntos[i][0], puntos[i][1],puntos[j][0], puntos[j][1])
			dists[i][j] = int(valor)

def createLinks(path):
    mn = len(path)
    ret = []
    for i in range(mn -1):
        ret.append({"source": path[i], "target": path[i+1]})
    return ret

def createNodes(node):
    ret = []
    for i in node:
        x = i[1]
        y = -i[0]
        idx = i[2]
        ret.append({"x": x, "y": y, "cod": idx})
    return ret

def crearLugar(distancias):
    ret = []
    for i in distancias:
        ret.append( { "CODLOCAL" : i[0], "CEN_EDU" : i[1], "CODCPSIG" : i[2], "NOMCPSIG" : i[3]} )
    return ret
			

puntos = []
csv2txt(puntos)
dists = [0]*n
for i in range(n):
	dists[i] = [0]*n
crear(dists, puntos)
ans, path = HK(dists)
path = path[::-1]

nd = createNodes(puntos)
lk = createLinks(path)

data = {"nodes": nd, "links": lk}
with open('graph17.json', 'w') as outfile:
    json.dump(data, outfile)

lg = crearLugar(puntos)
data = {"lugar": lg}
with open('info.json', 'w') as outfile:
    json.dump(data, outfile)

nombres = []
for a in puntos:
    nombres.append(a[3])

print(ans, path)
print("--- %s seconds ---" % (time.time() - start_time))