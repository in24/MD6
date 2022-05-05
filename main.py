# Moduļi
import PySimpleGUI as sg
sg.theme('DarkAmber')
import csv

# Klases
class Izskats:
	def __init__(self, logs, izkartojums):
		# vispārējie
		self.logs = logs
		self.izkartojums = izkartojums
		# lokālie
		self.notikums = None
		self.vertibas = None
		while True:
			self.notikums, self.vertibas = self.logs.read()
			if self.notikums == sg.WIN_CLOSED or self.notikums == 'Cancel':
				break
			else:
				sg.popup('Tu ievadīji', self.vertibas[0])   
class Komponente:
	def __init__(self, veids, modelis, razotajs, spec, cena):
		self.veids = veids
		self.modelis = modelis
		self.razotajs = razotajs
		self.spec = spec
		self.cena = cena
	# Komponentes metodes	
	def raksta(self, faila_vards):
		with open(faila_vards, "a") as fails:
			lauki = ["Veids", "Razotajs", "Modelis", "Spec", "Cena"]
			rakstitajs = csv.DictWriter(fails, fieldnames=lauki,delimiter=",")
			rakstitajs.writerow({"Veids":self.veids, "Razotajs":self.razotajs, "Modelis":self.modelis, "Spec":self.spec, "Cena":self.cena})
	def lasa(self, faila_vards):
		with open(faila_vards, "r") as fails:
			lasitajs = csv.DictReader(fails)
			for rinda in lasitajs:
				print(rinda)
				# Te jāsameklē, kā formā raksta sg.Table
	def redige(self, faila_vards):
		pass
	def dzes(self, faila_vards):
		pass
class Dators:
	def __init__(self, atmina, ram, gpu, cpu, mb, bloks, korpuss, cits):
		self.atmina = atmina
		self.ram = ram
		self.gpu = gpu
		self.cpu = cpu
		self.mb = mb
		self.bloks = bloks
		self.korpuss = korpuss
		self.cits = cits
	def saglaba(self):
		with open("dators.csv","w") as fails:
			lauki = ["Veids", "Razotajs", "Modelis", "Spec", "Cena"]
			rakstitajs = csv.DictWriter(fails, fieldnames=lauki,delimiter=",")
			rakstitajs.writeheader()
			#rakstitajs.writerow({"Veids":self.veids, "Razotajs":self.razotajs, "Modelis":self.modelis, "Spec":self.spec, "Cena":self.cena})
	def parskata(self):
		with open("dators.csv","r") as fails2:
			lasitajs = csv.DictReader(fails2)
			print ("Veids", "Razotajs", "Modelis", "Spec", "Cena")
			for rinda in lasitajs:
				print(rinda["Veids"], rinda["Razotajs"], rinda["Modelis"], rinda["Spec"], rinda["Cena"])

# Metodes
def main():
	izkartojums = [  [sg.Text('Komponentes')],
				   [sg.Text('Veids'), sg.InputText()],
				   [sg.Text('Ražotājs'), sg.InputText()],
				   [sg.Text('Modelis'), sg.InputText()],
				   [sg.Text('Specifikācija'), sg.InputText()],
				   [sg.Text('Cena'), sg.InputText()],
				   [sg.Button('Ok'), sg.Button('Cancel')] ]
	
	logs = sg.Window('Komponenšu logs', izkartojums)

	#komponentes_izskats = Izskats(izkartojums, logs)
	while True:
		notikums, vertibas = logs.read()
		if notikums == sg.WIN_CLOSED or notikums == 'Cancel':
			break
		else:
			sg.popup('Tu ievadīji', vertibas[0])  
	logs.close()
	
def Veca_programma():
	print("Labrīt!")
	d = input("Ievadi dienu: ")
	diena = Diena(d)
	diena.dienas_sakums()
	atverts = True
	while atverts:
		v = input("Ievadi vārdu (vai CIET, ja slēdz klubu): ")
		if v=="CIET":
			atverts = False
			break
		if v == "PR":
			diena.druka()
			break
		vec = int(input("Ievadi vecumu: "))
		cilveks = Persona(v,vec)
		cilveks.pieraksta(diena.diena+".csv")
	print("Jauku vakaru!")	

# Programma
#main()
#lasa()
#meginu = Komponente("Incanti","Mode","Raža","Garšviela",7.26)
#meginu.lasa("komponentes.csv")