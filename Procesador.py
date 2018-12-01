import sys


RAM = [[-1]*6 for _ in range(6)]		#Matriz de la ram (unicamente guarda a el id del proceso al que esta asignada)
VR = [[-1]*6 for _ in range(4)]			#Matriz de la memoria virtual la misma historia

def findID(tabla_de_procesos , id):					#Regresa en indice de un id dado, -1 si no existe
	for i in range(len(tabla_de_procesos)):
		if(tabla_de_procesos[i].id == id):
			return i
	return -1

def toFisic(p,s,w):
	x = int((((6*p)+(s%6))*4096)+w)
	ans = ""
	while(x > 0):
		y = int(x%16)
		if(y < 10):
			ans = str(y)+ans
		else:
			ans = chr(int(y-10+65))+ans
		x = x//16
	for i in range(8 - len(ans)):
		ans = "0"+ans;
	ans = "0x"+ans
	return ans

class fila_proceso():								#Define la informacion de cada bloque del proceso
	def __init__(self):
		self.memoria_usada = 'x'					#Tipo de memoria donde se almacena ('R' == ram , 'V' == virtual , 'x' == No asignada)
		self.pagina = -1							#Demaciado ovio
		self.segmento = -1
	def __init__(self,M,P,S):
		self.memoria_usada = M
		self.pagina = P
		self.segmento = S

class proceso():
	def __init__(self , a , _id):
		self.id = _id;					#Id unico del proceso
		self.size = a;					#Tamaño en en memoria del proceso
		self.proc_table = []					#Tabla de guarda cada fila de proceso con sus respectivas direcciones
	
	def assign(self,a):					#Guarda un proceso en RAM. Regresa True si todo el proceso se asigna en ram,
		if(a <= 4):						#asi mismo inserta en la matriz el id del proceso, regresa False en caso
			for i in range(6):			# de no entrar en la matriz
				for j in range(6):
					if(RAM[i][j] == -1):
						RAM[i][j] = self.id
						self.proc_table.append(fila_proceso('R',i,j))
						return True
			return False
		else:
			for i in range(6):
				for j in range(6):
					if(RAM[i][j] == -1):
						RAM[i][j] = self.id
						if(self.assign(a-4)):
							self.proc_table.append(fila_proceso('R',i,j))
							return True
						else:
							RAM[i][j] = -1;
							return False
	
	def assignV(self,a):					#Guarda un proceso en RAM. Regresa True si todo el proceso se asigna en ram,	
		if(a <= 4):							#asi mismo inserta en la matriz el id del proceso, regresa False en caso
			for i in range(4):				# de no entrar en la matriz
				for j in range(6):
					if(VR[i][j] == -1):
						VR[i][j] = self.id
						self.proc_table.append(fila_proceso('V',i,j))
						return True
			return False
		else:
			for i in range(6):
				for j in range(6):
					if(VR[i][j] == -1):
						VR[i][j] = self.id
						if(self.assignV(a-4)):
							self.proc_table.append(fila_proceso('V',i,j))
							return True
						else:
							VR[i][j] = -1;
							return False


	def clear(self):									#Borra el proceso de memoria, no lo elimina
		for i in self.proc_table:
			if(i.memoria_usada == 'R'):
				RAM[i.pagina][i.segmento] = -1;
			elif(i.memoria_usada == 'V'):
				VR[i.pagina][i.segmento] = -1;
			else:
				print("Memoria no asignada.")
		self.proc_table.clear()

	def swap(self,type):		#intercambia de memoria el proceso, en caso de no ser posible lo regresa a su estado inicial
		self.clear()
		if(type == 0):
			if(not self.assignV(self.size)):
				swap(1)
		else:
			if(not self.assign(self.size)):
				swap(0)

	def showInfo(self):
		x = 0
		listOfData = []
		for i in reversed(self.proc_table): 
			ans = ""
			if(i.memoria_usada == 'R'):
				ans += "RAM\t"
			elif(i.memoria_usada == 'V'):
				ans += "VIRTUAL\t"
			else:
				ans += "NO ASIGNADA\t"
			ans += str(i.pagina+1) + "\t"
			ans += str(i.segmento+1) + "\t"
			ans += toFisic(x//6,x,0)+"\t"
			ans += toFisic(i.pagina,i.segmento,367)
			listOfData.append(ans)
			print(ans)
			x += 1
		return listOfData


op = int(1)
t = 1;
noProcesos = 0;
idProcesos = 0;
proc = []
while(t):

	print("Menu:\n1.- Crear proceso.\n2.-Eliminar proceso.\n3.-Pasar proceso a memoria virtual.\n4.-Regresar proceso a memoria principal.\n5.-Salir.")
	op = int(input())
	if(op == 1):
		print("Dame el tamaño del proceso")
		op = int(input())
		proc.append(proceso(op,idProcesos+1))
		if(proc[noProcesos].assign(proc[noProcesos].size)):
			noProcesos += 1;
			idProcesos += 1;
		else:
			proc.pop()
	elif(op == 2):
		print("Dame el id del proceso")
		op = int(input())
		ind = findID(proc,op)
		if(ind != -1):
			proc[ind].clear()
			proc.pop(ind)				#Borra el proceso
			noProcesos -= 1;
		else:
			print("indice no valido")

	elif(op == 3):
		print("Dame el id del proceso")
		op = int(input())
		ind = findID(proc,op)
		if(ind != -1):
			proc[ind].swap(0)
		else:
			print("indice no valido")
	elif(op == 4):
		print("Dame el id del proceso")
		op = int(input())
		ind = findID(proc,op)
		if(ind != -1):
			proc[ind].swap(1)
		else:
			print("indice no valido")
	elif(op == 5):
		t = 0
	elif(op == 6):								#Usado para debug
		for i in RAM:
				for j in i:
					sys.stdout.write(str(j)+" ")
				print("\n")
		print("\n")
		for i in VR:
			for j in i:
				sys.stdout.write(str(j)+" ")
			print("\n")
	elif(op == 7):
		print("Dame el id del proceso")
		op = int(input())
		ind = findID(proc,op)
		if(ind != -1):
			proc[ind].showInfo()
		else:
			print("indice no valido")
