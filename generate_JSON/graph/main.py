import time
start_time = time.time()

from greedy import solve_tsp
import math
import csv
import json

ids = []
n = 1500
paso = int(145000/n)

def csv2txt(distancias, n):
    with open('cod_xy.csv') as file:
        reader = csv.reader(file)
        cont = 0
        p = 1
        for fila in reader:
            if p == paso:
                if cont != 0:
                    f = fila[0].split(";")
                    ids.append(f[0])
                    x = float(f[2])*100.0
                    y = float(f[1])*100.0
                    distancias.append((x,y))
                if cont>n:
                    break
                cont+=1
                p = 0
            p+=1

def cal_dis(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def getJsonGraph():
    distancias = []
    D = []
    for i in range(n):
        aux = []
        for j in range(n):
            aux.append(0)
        D.append(aux)

    csv2txt(distancias, n)
    i = 0
    while(i < n):
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
        i += 1

    path = (solve_tsp( D ))

    nd = createNodes(distancias)
    lk = createLinks(path)

    data = {"nodes": nd, "links": lk}
    with open('output.json', 'w') as outfile:
        json.dump(data, outfile)

    suma = 0
    for i in range(len(path)-1):
        x1 = distancias[path[i]][0]
        y1 = distancias[path[i]][1]
        x2 = distancias[path[i+1]][0]
        y2 = distancias[path[i+1]][1]
        suma = suma  + (cal_dis(x1,y1,x2,y2))
    
    print(suma)

    pt = []
    for i in path:
        pt.append(i)
    fpt = [{"node": pt}]
    with open('path.json', 'w') as outfile:
        json.dump(fpt, outfile)
    
    return

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
        x = d[i][0]
        y = -d[i][1]
        ret.append({"x": x, "y": y})
    return ret

getJsonGraph()

print("--- %s seconds ---" % (time.time() - start_time))

