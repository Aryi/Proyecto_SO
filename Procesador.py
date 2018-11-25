import sys


RAM = [[-1]*6 for _ in range(6)]
VR = [[-1]*6 for _ in range(4)]

def findID(tabla_de_procesos , id):
	for i in range(len(tabla_de_procesos)):
		if(tabla_de_procesos[i].id == id):
			return i
	return -1


class fila_proceso():
	def __init__(self):
		self.memoria_usada = 'x'
		self.pagina = -1
		self.segmento = -1
	def __init__(self,M,P,S):
		self.memoria_usada = M
		self.pagina = P
		self.segmento = S

class proceso():
	def __init__(self , a , _id):
		self.id = _id;
		self.size = a;
		self.proc_table = []
	
	def assign(self,a):
		print(a)
		if(a <= 4):
			for i in range(6):
				for j in range(6):
					if(RAM[i][j] == -1):
						print(str(i) + " , " + str(j))
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
			
	def clear(self):
		for i in self.proc_table:
			if(i.memoria_usada == 'R'):
				RAM[i.pagina][i.segmento] = -1;
			elif(i.memoria_usada == 'V'):
				VR[i.pagina][i.segmento] = -1;
			else:
				print("Memoria no asignada.")




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
			proc.pop(ind)
			noProcesos -= 1;
		else:
			print("indice no valido")

	elif(op == 3):

	elif(op == 4):
		for i in RAM:
				for j in i:
					sys.stdout.write(str(j)+" ")
				print("\n")
	elif(op == 5):
		t = 0
