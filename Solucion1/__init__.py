from greedy import solve_tsp
import math
import csv

n = 1500

def csv2txt(distancias):
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
				distancias.append((x,y))
			if cont>n:
				break
			cont+=1

	with open('info.txt', 'w') as file:
		for i in ids:
			file.write(str(i))

def cal_dis(x1,y1,x2,y2):
	return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

distancias = []
D = []
for i in range(n):
	aux = []
	for j in range(n):
		aux.append(0)
	D.append(aux)

csv2txt(distancias)

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
		#print(dis_aux)


path = solve_tsp( D )
print(path)
suma = 0
for i in range(len(path)-1):
	x1 = distancias[path[i]][0]
	y1 = distancias[path[i]][1]
	x2 = distancias[path[i+1]][0]
	y2 = distancias[path[i+1]][1]
	suma = suma  + (cal_dis(x1,y1,x2,y2))

print("Distancia recorrida ", suma)
