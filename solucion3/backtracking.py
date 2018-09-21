import csv
import math
#complejidad -> ya que tenemos n+1 espacios que llenar en nuestra configuraciones
# y en cada uno podemos poner n numeros indexados 0 - n-1 
#tenemos un tiempo promedio de O(n!) ademas de ello para cada configuracion
#queremos guardar la distancia que se recorrio con esa haciendo suma de todas las
#distancias que es una complejidad n asi que al final es O(n!x n) o O(n! + n)no 
#estoy segura creo que la primera
n = 10
posibles_ans = []
configuraciones = [0]*n

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
	for i in range(n-1):
		i1 = configuraciones[i]
		i2 = configuraciones[i+1]
		suma = suma + cal_dis(distancias[i1][0],distancias[i2][0],distancias[i1][1],distancias[i2][1])
	posibles_ans.append(suma)
	
def tsp(pos, distancias): 
	if(pos==n-1):
		verificar(distancias)
		return
	for i in range(1,n+1):
		configuraciones[pos] = i
		tsp(pos+1, distancias)
		configuraciones[pos] = -1

#main
distancias = []
csv2txt(distancias)
configuraciones[0] = configuraciones[n-1] = 0 #empieza en ciudad indexada 0
tsp(0, distancias)
sorted(posibles_ans)
print("bt <-> brute force", posibles_ans[0]) #la menor suma
