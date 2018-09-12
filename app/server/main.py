
from greedy import solve_tsp
import math
import csv
import json

def csv2txt(distancias, n):
	ids = []
	with open('../server/informacion.csv') as file:
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
	with open('../server/info.txt', 'w') as file:
		for i in ids:
			file.write(str(i))

def cal_dis(x1,y1,x2,y2):
	return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def getJsonGraph(txt):
    n = 1500
    distancias = []
    D = []
    for i in range(n):
    	aux = []
    	for j in range(n):
    		aux.append(0)
    	D.append(aux)

    csv2txt(distancias, n)

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

    path = (solve_tsp( D ))

    nd = createNodes(distancias)
    lk = createLinks(path)

    data = {"nodes": nd, "links": lk}

    return json.dumps(data)

def createLinks(p):
    n = len(p)
    ret = []
    for i in range(1,n):
        ret.append({"source": p[i], "target": p[i-1]})
    return ret

def createNodes(d):
    n = len(d)
    ret = []
    for i in range(1,n):
        ret.append({"x": d[i][0], "y": d[i][0]})
    return ret
