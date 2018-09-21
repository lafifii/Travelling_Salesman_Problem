import csv
import math

INT_MAX  = 999999
n=20
#COMPLEJIDAD O(2^n * n^2) puede resolver el problema hasta lo que alcanze un 
#long long para el mask
#resuelve el problema hasta un 0.013 % con un tiempo prudente en este ejemplo
#ya que cada 10^8 es un segundo aproximado con 2^8 * 8^2 tenemos 1048576 + 64 iteraciones
#que es mas de 10^9 incluso por lo que cada 20 ciudades se demorara mas de un segundo
#y esto crece exponencialmente muy rapido ya que se hablan de potencias de 2
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

