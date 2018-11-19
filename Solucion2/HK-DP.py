import itertools
import random
import sys
import csv
import math
from collections import namedtuple
from operator import itemgetter 
import time
start_time = time.time()

n = 1
#O(n^2 * 2^n) Complejidad ,  2^n * n Espacio.
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

def HK(dists):
    global n
    C = {}
    for k in range(1, n):
        C[(1 << k,k)] = (dists[0][k], 0)

    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
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
        aux , parent = C[(bits, parent)]
        bits = new_bits

    path.append(0)

    return opt, path

def cal_dis(x1,y1,x2,y2):
	return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def crear(dists, puntos):
	for i in range(n):
		for j in range(n):
			valor = cal_dis(puntos[i][0], puntos[i][1],puntos[j][0], puntos[j][1])
			dists[i][j] = int(valor)

			

puntos = []
csv2txt(puntos)
dists = [0]*n
for i in range(n):
	dists[i] = [0]*n
crear(dists, puntos)
ans, path = HK(dists)
path = path[::-1]
print(ans, path)
print("--- %s seconds ---" % (time.time() - start_time))