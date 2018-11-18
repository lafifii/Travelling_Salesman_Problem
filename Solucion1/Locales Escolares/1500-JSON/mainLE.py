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
paso = int(75000/n)

def csv2txt():
    distancias = []
    node = []
    global n
    global paso
    with open('LE.csv') as file:
        reader = csv.reader(file)
        cont = 0
        p = 1
        for fila in reader:
            if p == paso:
                if cont != 0:
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
        ret.append( { "CODCPSIG": i[2], "CEN_EDU_L": i[3], "NOMCPSIG": i[4]} )
    return ret

node, distancias = csv2txt()

path, w = TSP_DPC.TSP(node)

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
