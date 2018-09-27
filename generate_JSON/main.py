import time
start_time = time.time()

import math
import csv
import json
import sys

csv.field_size_limit(sys.maxint)

n = 1500
paso = int(145000/n)
visitado = [False]*n

def csv2txt(distancias):
    global n
    global paso
    with open('data.csv') as file:
        reader = csv.reader(file)
        cont = 0
        p = 1
        for fila in reader:
            if p == paso:
                if cont != 0:
                    f = fila[0].split(";")
                    if len(f)>=8:
                        CODCP = int(f[0])
                        DEP = f[1]
                        PROV = f[2]
                        DIST = f[3]
                        NOMCP = f[4]
                        MNOMCP = f[5]
                        y = float(f[6])*100.0
                        x = float(f[7])*100.0
                        distancias.append([x, y, CODCP, DEP, PROV, DIST, NOMCP, MNOMCP])
                    else:
                        print(f)
                        p-=1
                        continue
                if cont>n:
                    break
                cont+=1
                p = 0
            p+=1


def cal_dis(x1,y1,x2,y2):
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def solve_tsp(distancias):
    global n
    n = len(distancias)
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

def createLinks(p):
    mn = len(p)
    ret = [{"source": p[mn-1], "target": p[0]}]
    for i in range(1,mn):
        ret.append({"source": p[i], "target": p[i-1]})
    return ret

def createNodes(d):
    ret = []
    i = 0
    for i in range(n):
        x = d[i][1]
        y = -d[i][0]
        idx = d[i][2]
        ret.append({"x": x, "y": y, "cod": idx})
    return ret

def crearLugar(distancias):
    ret = []
    for i in distancias:
        ret.append( { "CODCP": i[2], "DEP": i[3], "PROV": i[4], "DIST": i[5], "NOMCP": i[6], "MNOMCP": i[7]} )
    return ret

distancias = []

csv2txt(distancias)

suma, path = solve_tsp(distancias)
coordenadas_en_orden_del_path = []
pathcoordenadas(coordenadas_en_orden_del_path, path, distancias)

print("Distancia recorrida ", suma)

nd = createNodes(coordenadas_en_orden_del_path)
lk = createLinks(path)

data = {"nodes": nd, "links": lk}
with open('graph.json', 'w') as outfile:
    json.dump(data, outfile)

pt = []
for i in path:
    pt.append(i)
fpt = [{"node": pt}]
with open('path.json', 'w') as outfile:
    json.dump(fpt, outfile)

lg = crearLugar(distancias)
data = {"lugar": lg}
with open('info.json', 'w') as outfile:
    json.dump(data, outfile, encoding='latin1')

print("--- %s seconds ---" % (time.time() - start_time))
print("nodos:",n);
