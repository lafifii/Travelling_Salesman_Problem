import time
start_time = time.time()

import math
import csv
import json
import sys
import TSP_DPC

#csv.field_size_limit(sys.maxsize)
csv.field_size_limit(2147483647)

n = 0

def csv2txt():
    distancias = []
    node = []
    global n
    global paso
    cont = 0
    limit = 5000
    with open('LE.csv') as file:
        reader = csv.reader(file)
        for fila in reader:
            if cont >= limit:
                break
            f = fila[0].split(";")
            if len(f)>=5:
                try:
                    CODCP = int(f[0]) # CODCPSIG
                except ValueError:
                    print("Except: ", ValueError)
                    break
                CEN = f[1] # CEN_EDU_L
                NOM = f[2] # NOMCPSIG
                y = float(f[3])*100.0
                x = float(f[4])*100.0
                distancias.append([x, y, CODCP, CEN, NOM])
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
        ret.append( { "CODCPSIG": i[2], "CEN_EDU_L": i[3], "NOMCPSIG": i[4]} )
    return ret

node, distancias = csv2txt()

path, w = TSP_DPC.TSP(node)

print("Distancia recorrida: ", w)

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
print("nodos:",n);
