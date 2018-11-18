import time
start_time = time.time()

import math
import csv
import json
import sys
import TSP_DPC

#csv.field_size_limit(sys.maxsize)
#csv.field_size_limit(sys.maxint)
csv.field_size_limit(2147483647)
n = 0

def csv2txt():
    distancias = []
    node = []
    global n
    limit = 5000
    cont = 0
    with open('CP_flag.csv') as file:
        reader = csv.reader(file)
        for fila in reader:
                if cont >= limit:
                    break
                f = fila[0].split(";")
                if len(f)>=8:
                    try:
                        CODCP = int(f[0])
                    except ValueError:
                        continue
                    DEP = f[1]
                    PROV = f[2]
                    DIST = f[3]
                    NOMCP = f[4]
                    MNOMCP = f[5]
                    y = float(f[6])*100.0
                    x = float(f[7])*100.0
                    distancias.append([x, y, CODCP, DEP, PROV, DIST, NOMCP, MNOMCP])
                    node.append((x,y,CODCP))
                    cont += 1
                else:
                    print(f)
                    continue
    n = len(node)
    return node, distancias

def createLinks(path):
    mn = len(path)
    ret = []
    for i in path:
        ret.append({"source": i[0], "target": i[1]})
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
        ret.append( { "CODCP": i[2], "DEP": i[3], "PROV": i[4], "DIST": i[5], "NOMCP": i[6], "MNOMCP": i[7]} )
    return ret

node, distancias = csv2txt()

path, w = TSP_DPC.TSP(node)
print(w)

print("Distancia recorrida: ", w)

# Descomentar para generar el json
"""
nd = createNodes(node)
lk = createLinks(path)

data = {"nodes": nd, "links": lk}
with open('graph.json', 'w') as outfile:
    json.dump(data, outfile)

lg = crearLugar(distancias)
data = {"lugar": lg}
with open('info.json', 'w') as outfile:
    json.dump(data, outfile)

nombres = []
for a in distancias:
    nombres.append(a[3])
"""

print("--- %s seconds ---" % (time.time() - start_time))
print("nodos:",n)
