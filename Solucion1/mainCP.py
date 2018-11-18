#!/usr/bin/env python3

import time
start_time = time.time()

import math
import csv
import json
import sys
import TSP_DPC

#csv.field_size_limit(sys.maxsize)
csv.field_size_limit(sys.maxsize)

n = 1500
paso = int(150000/n)

def csv2txt():
    distancias = []
    node = []
    global n
    global paso
    with open('CP.csv') as file:
        reader = csv.reader(file)
        cont = 0
        p = 1
        for fila in reader:
            if p == paso:
                if cont != 0:
                    f = fila[0].split(";")
                    if len(f)>=8:
                        try:
                            CODCP = int(f[0])
                        except ValueError:
                            print("Except: ", ValueError)
                            break
                        DEP = f[1]
                        PROV = f[2]
                        DIST = f[3]
                        NOMCP = f[4]
                        MNOMCP = f[5]
                        y = float(f[6])*100.0
                        x = float(f[7])*100.0
                        distancias.append([x, y, CODCP, DEP, PROV, DIST, NOMCP, MNOMCP])
                        node.append((x,y,CODCP))
                    else:
                        print(f)
                        p-=1
                        continue
                if cont>n:
                    break
                cont+=1
                p = 0
            p+=1
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

# Descomentar para generar el json
print("Distancia recorrida: ", w)

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

print("--- %s seconds ---" % (time.time() - start_time))
print("nodos:",n);
