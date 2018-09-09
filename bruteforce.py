import csv
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial as spatial
from collections import defaultdict
from collections import deque
import sys
import signal,os

class departamento:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def calcularDistancia(otro):
		return sqrt((x-otro.x)*(x-otro.x) + (y-otro.y)*(y-otro.y,2))

class tsp:
	def csv2txt(distancias):
		ids = []
		with open('informacion.csv') as file:
			reader = csv.reader(file)
			cont = 0
			for fila in reader:
				if cont != 0:
					alo = str(cont) +"," + fila[3] + "\n"
					ids.append(alo)
					x = float(fila[15])*10000
					y = float(fila[16])*10000
					distancias.append(departamento(x,y))
				if cont>150:
					break
				cont+=1

		with open('info.txt', 'w') as file:
			for i in ids:
				file.write(str(i))

	def __init__(self):
		self.listo = False
		self.distancias = []
		self.n = 0
		self.solucion = deque()


	def inicializar(self):
		csv2txt(distancias)
		n = len(distancias)

	def fuerza_bruta_wrapper(self):
		total_distancia = 0
		min_distancia = 999999999
		besto = deque()
		if count(solucion) == 0:
			knn()
		
		fuerza_bruta(besto, min_distancia, self.n)
		guardar_solucion(besto, self.solucion)

		total_distancia = getDistancia()
		return total_distancia

	def fuerzaBruta(besto,min_distancia,nciudades):

		acumulado = 0
		signal.signal(signal.SIGALARM, finnn)
		i = 0
		while(listo and i<nciudades):
			rotate(nciudades-1)
			acumulado = getDistancia()
			if(acumulado < min_distancia):
				min_distancia = acumulado
				print(min_distancia)
				guardar_solucion(self.solucion, besto)
			fuerzaBruta(besto, min_distancia, nciudades-1)
			i = i+1

	def rotate(pos):
		solucion.appendleft(solucion[pos])
		del solucion[pos+1]


	def getDistancia():
		total_distancia = 0
		for i in range(nciudades-1):
			total_distancia = total_distancia + solucion[i].calcularDistancia(solucion[i+1])
		total_distancia = total_distancia + solucion[0].calcularDistancia(solucion[nciudades-1])

		return total_distancia

	def guardar_solucion(fuente, dest):
		ll = count(fuente)
		dest.clear()
		for i in range(ll):
			dest.append(departamento(fuente[i]))

	def finnn(signum, frame):
		done = True



	def knn(nn):
		tree = spatial.cKDTree(distancias)   
		for i in range(nn,self.n):        
			dist, ind = tree.query(distancias[i], k=5)
			make_pairs(ind,dist,k,grafo,i)



	def make_pairs(ind,dist,k,grafo,i):
		arrpairs = []
		for __kk__ in range(5):
			if ind[__kk__] != i:
				grafo[i].append((ind[__kk__], round(dist[__kk__])))



def printLAD(grafo,n):
	for i in range(n):
		for elem in grafo[i]:
			print(elem, end="  ")
		print("")

tspobj = tsp()
tspobj.inicializar()
tspobj.fuerza_bruta_wrapper()




