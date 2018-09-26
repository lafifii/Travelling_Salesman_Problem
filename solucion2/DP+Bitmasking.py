import csv
import math

INT_MAX  = 999999
n=20
#COMPLEJIDAD maximo valor del mask * pos = 1048576 * 20 , es un algortimo eficiente
#pero usa variables muy grandes ya que en la mascara cada 1 es una ciudad ya visitada
# entonces si es 20 el numero de ciudades el numero del mask debe ser 
# 2 + 4 + 8 + 16 + 32 ..... 2^20 = 1048576 y solo soporta hasta el numero maximo
#que pueda soportar un long long osea 64 ciudades como maximo
dist = [[0 for x in range(140)] for y in range(140)]
todos_vis = (1<<n) -1;
dp = [[0 for x in range(20)] for y in range(1048576)]

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

def tsp(mask,pos): 
	global dp,INT_MAX,todos_vis
	if(mask==todos_vis):
		return dist[pos][0]
	if(dp[mask][pos]!=-1):
	   return dp[mask][pos]
	ans = INT_MAX;
	for ciudad in range(n):
		if((mask&(1<<ciudad))==0):
			ans2 = dist[pos][ciudad] + tsp( mask|(1<<ciudad), ciudad);
			ans = min(ans, ans2);

	dp[mask][pos] = ans
	return dp[mask][pos];

def cal_dis(x1,y1,x2,y2):
	return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def rec(mask,pos, s): 
	global dp,INT_MAX,todos_vis

	if(mask==todos_vis):
		return dist[pos][0]
	
	if(dp[mask][pos]!=-1):
	   return dp[mask][pos]
	
	ans = INT_MAX;
	for ciudad in range(n):
		if((mask&(1<<ciudad))==0):
			ans2 = dist[pos][ciudad] + tsp( mask|(1<<ciudad), ciudad);
			if(ans2<ans):
				s = s + str(ciudad)

#main
distancias = []
csv2txt(distancias)
for i in range(n):
	for j in range(n):
		dist[i][j] = cal_dis(distancias[i][0],distancias[j][0],distancias[i][1],distancias[j][1]) 

for i in range(1<<n): #2 a la n
	for j in range(n):
		dp[i][j] = -1;

print("tsp dp + bitmasking ", tsp(1,0))
s = ""
rec(1,0,s)
print(s)
