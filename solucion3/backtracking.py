import csv
import math
from operator import itemgetter
#complejidad -> ya que tenemos n+1 espacios que llenar en nuestra configuraciones
# y en cada uno podemos poner n numeros indexados 0 - n-1 
#tenemos un tiempo promedio de O(n!) ademas de ello para cada configuracion
#queremos guardar la distancia que se recorrio con esa haciendo suma de todas las
#distancias que es una complejidad n asi que al final es O(n!x n)  

n = 10
posibles_ans = []
cont = 0
cadenas = []
visitado = [False]*20
configuraciones = [0]*20

def csv2txt(distancias):
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
				distancias.append((x,y))
			if cont>n:
				break
			cont+=1

	with open('info.txt', 'w') as file:
		for i in ids:
			file.write(str(i))

def cal_dis(x1,y1,x2,y2):
	return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def verificar(distancias):
	suma = 0
	AUX = []
	for i in range(n-1):
		AUX.append(configuraciones[i])
		i1 = configuraciones[i]
		i2 = configuraciones[i+1]
		suma = suma + cal_dis(distancias[i1][0],distancias[i2][0],distancias[i1][1],distancias[i2][1])
	#print("fi")
	AUX.append(configuraciones[n-1])
	posibles_ans.append(tuple((suma, cont)))
	cadenas.append(AUX)

def tsp(pos, distancias): 
	if(pos==n-1):
		#print("gyu")
		verificar(distancias)
		return

	for i in range(1,n+1):
		#print(visitado[i])
		if(visitado[i] == False):
			configuraciones[pos] = i
			visitado[i] = True
			tsp(pos+1, distancias)
			configuraciones[pos] = -1
			visitado[i] = False

#main
distancias = []
csv2txt(distancias)
configuraciones[0] = configuraciones[n-1] = 0 #empieza en ciudad indexada 0
for i in range(n):
	visitado[i] = False

visitado[0] = True
tsp(0, distancias)
posibles_ans.sort(key=itemgetter(0))
print("bt <-> brute force", posibles_ans[0][0]) #la menor suma
print(cadenas[posibles_ans[0][1]])
