import math
import csv
import json
import sys

csv.field_size_limit(sys.maxint)
# CODCP DEP PROV DIST NOMCP MNOMCP

dat = []
n = 1500
paso = int(145000/n)

def csv2txt():
    with open('cod_info.csv') as file:
        reader = csv.reader(file)
        cont = 0
        p = 1
        for fila in reader:
            if p == paso:
                if cont != 0:
                    f = fila[0].split(";")
                    C = f[0]
                    De = f[1]
                    P = f[2]
                    Di = f[3]
                    N = f[4]
                    M = f[5]
                    dat.append([C,De,P,Di,N,M])
                if cont>n:
                    break
                cont+=1
                p = 0
            p+=1

def getJsonGraph():
    lg = crearLugar()
    
    data = {"lugar": lg}
    with open('info.json', 'w') as outfile:
        json.dump(data, outfile, encoding='latin1')
    return

def crearLugar():
    n = len(dat)
    ret = []
    for i in range(n):
        ret.append( { "CODCP": dat[i][0], "DEP": dat[i][1], "PROV": dat[i][2], "DIST": dat[i][3], "NOMCP": dat[i][4], "MNOMCP": dat[i][5]} )
    return ret
csv2txt()
getJsonGraph()
