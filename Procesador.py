import sys
from tkinter import *
import copy
import tkinter as tk 
import random
from random import randrange
from tkinter import messagebox

#Variables globales
tabla_STR = "Memoria\t  Pagina\tSegmento\t  Direccion Virtual\t\tDireccion fisica\n"

#funciones del menu

t = 1;
noProcesos = 0;
idProcesos = 0;
proc = []

def Crear_Proceso():
    shell=Tk()
    shell.geometry('260x100')
    shell.title("Crear Proceso")
    tamaño = Label(shell, text='tamaño',font=(30))
    tamaño.place(x=10,y=5)
    tamañoE=Entry(shell, width="8")
    tamañoE.place(x=95,y=5)
    crear=Button(shell,text="Crear", command=lambda:crear_p(int(tamañoE.get())))
    crear.place(x=200,y=70)

    shell.mainloop

def Eliminar_Proceso():
    shell=Tk()
    shell.geometry('260x100')
    shell.title("Eliminar Proceso")
    idP = Label(shell, text='ID del proceso',font=(30))
    idP.place(x=10,y=5)
    idPE=Entry(shell, width="8")
    idPE.place(x=130,y=5)
    eliminar=Button(shell,text="Eliminar", command=lambda:eliminar_P(int(idPE.get())))
    eliminar.place(x=181,y=70)

    shell.mainloop

def Pasar_Mem_V():
    shellMV=Tk()
    shellMV.geometry('260x100')
    shellMV.title("Pasar proceso a memoria virtual")
    idP = Label(shellMV, text='ID del proceso',font=(30))
    idP.place(x=10,y=5)
    idPMVE=Entry(shellMV, width="8")
    idPMVE.place(x=130,y=5)
    PAS=Button(shellMV,text="Pasar a SWAP", command=lambda:Pasar_swap(int(idPMVE.get())))
    PAS.place(x=148,y=70)
    shellMV.mainloop

def Regresar_Mem_P():
    shell=Tk()
    shell.geometry('260x100')
    shell.title("Regresar proceso a memoria principal")
    idP = Label(shell, text='ID del proceso',font=(30))
    idP.place(x=10,y=5)
    idPE=Entry(shell, width="8")
    idPE.place(x=130,y=5)
    PAR=Button(shell,text="Regresar a RAM", command=lambda:Regresar_ram(int(idPE.get())))
    PAR.place(x=135,y=70)
    shell.mainloop


#fin de funciones de menu

#Ventana Principal
ventana=Tk()
ventana.title("Simulacion del funcionamiento de la memoria Ram con Swap")

#AnchoxAlto
ventana.geometry('1250x590')
ventana.configure(background='gray64')

tablapros=Text(ventana,width=20,height=40)
tablapros.grid(row=1,column=1)

scrollyTP=Scrollbar(ventana,command=tablapros.yview)
scrollyTP.grid(row=1, column=0, sticky="nsew")

tablapros.config(yscrollcommand=scrollyTP.set)
tablapros.insert("insert","Id proceso\t  Tamaño\n")
tablapros.config(state="disable")

#frames

admin_pros = Frame(ventana, bg='darkcyan', width=659, height=300, highlightbackground="white", highlightcolor="white", highlightthickness=2, bd=0, padx=3, pady=3)
admin_pros.place(x=705, y=0)

tablaadminpros=Text(admin_pros,width=90,height=19)
tablaadminpros.grid(row=1,column=0)

scrollyTAP=Scrollbar(admin_pros,command=tablaadminpros.yview)
scrollyTAP.grid(row=1, column=1, sticky="nsew")

tablaadminpros.config(yscrollcommand=scrollyTAP.set)
tablaadminpros.insert("insert",tabla_STR)
tablaadminpros.config(state="disable")


#Divicion virtual
#admin_mem = Frame(ventana, bg='slategray', width=659, height=300, highlightbackground="white", highlightcolor="white", highlightthickness=2, bd=0, padx=3, pady=3)
#admin_mem.place(x=705, y=300)

#Direccion fisica
#barra = Frame(ventana, bg='navy', width=659, height=300,highlightbackground="white", highlightcolor="white", highlightthickness=2, bd=0, padx=3, pady=3)
#barra.place(x=705, y=600)


#fin de frames

#Etiquetas
#Tabla de segmentos
procesos = Label(admin_pros, text='Descripcion de memoria', bg='darkcyan', fg="white")
procesos.grid(row=0, column=0)
#procesos.place(x=217, y=5, anchor='center')

#Divicion vitual
#memoria = Label(admin_mem, text='Divicion virtual')
#memoria.place(x=217, y=5, anchor='center')

#Direccion Fisica
#notifica = Label(barra, text='RAM')
#notifica.place(x=217, y=5, anchor='center')


#fin Etiquetas

#menu
barraMenu=Menu(ventana)

mnuArchivo=Menu(barraMenu,tearoff=0)

mnuArchivo.add_command(label="Crear Proceso", command=Crear_Proceso)
mnuArchivo.add_command(label="Eliminar Proceso", command=Eliminar_Proceso)
mnuArchivo.add_command(label="Pasar proceso a memoria virtual", command=Pasar_Mem_V)
mnuArchivo.add_command(label="Regresar proceso a memoria principal.", command=Regresar_Mem_P)
mnuArchivo.add_command(label="Salir")

barraMenu.add_cascade(label="Archivo", menu=mnuArchivo)

ventana.config(menu=barraMenu)
#fin del menu

def llenar_tabla_AdmP(ans):
	tabla=tablaadminpros
	tabla.config(state="normal")
	tabla.insert("insert",ans+"\n")
	tabla.config(state="disable")

def eliminar_tabla(tabla):
	tabla.config(state="normal")
	Memoria="111"
	pagina="22"
	segmento="3"
	DV="44444"
	DF="5"
	tabla.delete('1.0', END)
	tabla.insert("insert",tabla_STR)
	for i in range (0,3):
		tabla.insert("insert","111\t\t22\t\t3\t\t44444\t\t\t5\n")
	tabla.config(state="disable")


#Inicio de estructura de la memoria Ram#####################################################################################################3333

#etiqueta = Label(ventana)
#etiqueta.place(x=200, y=50)
randomColors =[[randrange(255),randrange(255),randrange(255)]for _ in range (200)]
color=("#%02x%02x%02x" % (randomColors[0][0],randomColors[0][1],randomColors[0][2]))
color2=("#%02x%02x%02x" % (randomColors[1][0],randomColors[1][1],randomColors[1][2]))

RamL=Label(ventana,text="RAM",font=(30),background='gray64')
RamL.place(x=408,y=5)
tablaRam=Frame(ventana, bg='black', width=400, height=300,)
tablaRam.place(x=300,y=30)

RAMT =[[Label(tablaRam) for _ in range(6)] for _ in range(6)]

for i in range(6):
    for j in range(6): 
    	RAMT[i][j]=Label(tablaRam,bg="red",width=6)
    	RAMT[i][j].grid(row=i, column=j, sticky=NSEW,padx=1, pady=1)

#RAMT[0][0].config(bg=color)

SwapL=Label(ventana,text="SWAP",font=(30),background='gray64')
SwapL.place(x=408,y=310)
tablaSwap=Frame(ventana, bg='black', width=400, height=300,)
tablaSwap.place(x=300,y=340)

SWAPT =[[Label(tablaRam) for _ in range (6)] for _ in range(4)]

for i in range(4):
    for j in range(6): 
    	SWAPT[i][j]=Label(tablaSwap,bg="red",width=6)
    	SWAPT[i][j].grid(row=i, column=j, sticky=NSEW,padx=1, pady=1)

#SWAPT[0][0].config(bg=color2)

###########################################################Funciones Procesador.py##################################################################################################
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
			for i in range(4):
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
				self.swap(1)
				return False
			else:
				return True
		else:
			if(not self.assign(self.size)):
				self.swap(0)
				return False
			else:
				return True


	def showInfo(self):
		tablaadminpros.config(state="normal")
		tablaadminpros.delete('1.0', END)
		tablaadminpros.insert("insert",tabla_STR)
		tablaadminpros.config(state="disable")
		x = 0
		y = 367
		listOfData = []
		for i in reversed(self.proc_table): 
			y = 367
			ans = ""
			if(i.memoria_usada == 'R'):
				ans += "  RAM\t"
			elif(i.memoria_usada == 'V'):
				y += 147456
				ans += "VIRTUAL\t"
			else:
				ans += "NO ASIGNADA\t"
			ans += "    "+str(i.pagina+1) + "\t"
			ans += "    "+str(i.segmento+1) + "\t"
			ans += "    "+toFisic(x//6,x,0)+"\t\t\t"
			ans += toFisic(i.pagina,i.segmento,y)
			listOfData.append(ans)
			x += 1
			llenar_tabla_AdmP(ans)
		return 

ver=[Button(ventana) for _ in range(200)]
y=0
def crear_p(op):
	global noProcesos
	global idProcesos
	global proc
	global tablapros
	global y
	id=noProcesos
	tablapros.config(state="normal")
	proc.append(proceso(op,idProcesos+1))
	if(proc[noProcesos].assign(proc[noProcesos].size)):
		noProcesos +=1;
		idProcesos +=1;
		tablapros.insert("insert",str(idProcesos)+"\t     "+str(op)+"\n")
		tablapros.config(state="disable")
		ver[idProcesos]= Button(ventana, text="ver"+str(idProcesos),command=lambda:proc[id].showInfo())
		ver[idProcesos].place(x=160,y=y)
		y+=27
		llenarRAM(idProcesos)
		messagebox.showinfo("AYE","Proceso Creado")
	else:

		for i in proc:
			if(i.id != idProcesos+1 and i.swap(0)):
				if(proc[noProcesos].assign(proc[noProcesos].size)):
					noProcesos +=1;
					idProcesos +=1;
					tablapros.insert("insert",str(idProcesos)+"\t     "+str(op)+"\n")
					tablapros.config(state="disable")
					ver[idProcesos]= Button(ventana, text="ver"+str(idProcesos),command=lambda:proc[id].showInfo())
					ver[idProcesos].place(x=160,y=y)
					y+=27
					llenarRAM(idProcesos)
					llenarSWAP(i.id)
					messagebox.showinfo("AYE","Proceso Creado")
					break
				else:
					i.swap(1)
			elif(i.id == idProcesos+1):
				if(i.assignV(i.size)):
					noProcesos +=1;
					idProcesos +=1;
					tablapros.insert("insert",str(idProcesos)+"\t     "+str(op)+"\n")
					tablapros.config(state="disable")
					ver[idProcesos]= Button(ventana, text="ver"+str(idProcesos),command=lambda:proc[id].showInfo())
					ver[idProcesos].place(x=160,y=y)
					y+=27
					llenarSWAP(idProcesos)
					messagebox.showinfo("AYE","Proceso Creado")
					break

def eliminar_P(op):
	global noProcesos
	global idProcesos
	global proc
	global y
	y=0
	ind = findID(proc,op)
	if(ind != -1):
		proc[ind].clear()
		proc.pop(ind)				#Borra el proceso
		noProcesos -= 1;
		tablapros.config(state="normal")
		tablapros.delete('1.0', END)
		tablapros.insert("insert","Id proceso\t  Tamaño\n")
		borrar_botons()
		#ver[op+1].place_forget()
		#ver.pop(op)
		posicion=[]
		for i in range(0,noProcesos):
			tablapros.insert("insert",str(proc[i].id)+"\t     "+str(proc[i].size)+"\n")
			if(i==0):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[0].showInfo())
			elif(i==1):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[1].showInfo())
			elif(i==2):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[2].showInfo())
			elif(i==3):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[3].showInfo())
			elif(i==4):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[4].showInfo())
			elif(i==5):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[5].showInfo())
			elif(i==6):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[6].showInfo())
			elif(i==7):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[7].showInfo())
			elif(i==8):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[8].showInfo())
			elif(i==9):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[9].showInfo())
			elif(i==10):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[10].showInfo())
			elif(i==11):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[11].showInfo())
			elif(i==12):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[12].showInfo())
			elif(i==13):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[13].showInfo())
			elif(i==14):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[14].showInfo())
			elif(i==15):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[15].showInfo())
			elif(i==16):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[16].showInfo())
			elif(i==17):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[17].showInfo())
			elif(i==18):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[18].showInfo())
			elif(i==19):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[19].showInfo())
			elif(i==20):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[20].showInfo())
			elif(i==21):
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[21].showInfo())
			else:
				ver[i+1]= Button(ventana, text="ver"+str(int(proc[i].id)),command=lambda:proc[i].showInfo())
			ver[i+1].place(x=160,y=y)
			#if(i!=op+1):
			ver[i+1].config(text="ver"+str(proc[i].id))
			y+=27
		tablapros.config(state="disable")
		llenarRAM(op)
		llenarSWAP(op)
		messagebox.showinfo("AYE","Proceso eliminado")
	else:
		messagebox.showinfo("Error","El id del proceso no existe")
def borrar_botons():
	global ver
	for i in range (0,idProcesos):
		ver[i+1].place_forget()	
	ver=[Button(ventana) for _ in range(40)]

def Pasar_swap(op):
	ind = findID(proc,op)
	if(ind != -1):
		proc[ind].swap(0)
		llenarSWAP(op)
		llenarRAM(op)
		messagebox.showinfo("AYE","Listo")
	else:
		messagebox.showinfo("Error","El id del proceso no esta en RAM")

def Regresar_ram(op):
	ind = findID(proc,op)
	if(ind != -1):
		proc[ind].swap(1)
		llenarRAM(op)
		llenarSWAP(op)
		messagebox.showinfo("AYE","Listo")
	else:
		messagebox.showinfo("Error","El id del proceso no esta en SWAP")

def llenarRAM(id):
	global RAM
	global randomColors
	color=("#%02x%02x%02x" % (randomColors[id][0],randomColors[id][1],randomColors[id][2]))
	for i in range(0,6):
		for j in range(0,6):
			if(RAM[i][j]==id):
				RAMT[i][j].config(bg=color,text=id)
			elif(RAM[i][j]==-1):
				RAMT[i][j].config(bg="red",text="")

def llenarSWAP(id):
	global VR
	global randomColors
	color=("#%02x%02x%02x" % (randomColors[id][0],randomColors[id][1],randomColors[id][2]))
	for i in range(0,4):
		for j in range(0,6):
			if(VR[i][j]==id):
				SWAPT[i][j].config(bg=color,text=id)
			elif(VR[i][j]==-1):
				SWAPT[i][j].config(bg="red",text="")
		
ventana.mainloop()




