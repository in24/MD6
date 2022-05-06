# (C) Grupa VP3, 2022

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

	def redige(self, faila_vards):
		pass
	def dzes(self, faila_vards):
		pass
class Dators:
	def __init__(self, atmina, ram, gpu, cpu, mb, bloks, korpuss):
		self.atmina = atmina
		self.ram = ram
		self.gpu = gpu
		self.cpu = cpu
		self.mb = mb
		self.bloks = bloks
		self.korpuss = korpuss
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
def Veca_programma():
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

	
def ievade():
	print ("Veids", "Razotajs", "Modelis", "Spec", "Cena")
	veids = input()
	razotajs = input()
	modelis = input()
	spec = input()
	cena = input()
	detala = Komponente(veids,razotajs,modelis,spec,cena)
	return detala
def lasa():
	with open("komponentes.csv", "r") as fails:
		lasitajs = csv.DictReader(fails)
		skaititajs = 1
		for rinda in lasitajs:
			print(skaititajs,"=",rinda)
			skaititajs += 1
def dzest(nr):
	saraksts = []
	with open("komponentes.csv", "r") as fails:
		lasitajs = csv.DictReader(fails)
		for rinda in lasitajs:
			saraksts.append(rinda)
		saraksts.pop(nr-1)
	with open("komponentes.csv","w") as fails1:
		lauki = ["Veids", "Razotajs", "Modelis", "Spec", "Cena"]
		rakstitajs = csv.DictWriter(fails1, fieldnames=lauki,delimiter=",")
		rakstitajs.writeheader()
		for ieraksts in saraksts:
			rakstitajs.writerow(ieraksts)	
def labot(nr):
	saraksts = []
	with open("komponentes.csv", "r") as fails:
		lasitajs = csv.DictReader(fails)
		for rinda in lasitajs:
			saraksts.append(rinda)
		print("Labojamā informācija:")
		print(saraksts[nr-1])
		saraksts.pop(nr-1)
		#print(saraksts)
	with open("komponentes.csv","w") as fails1:
		lauki = ["Veids", "Razotajs", "Modelis", "Spec", "Cena"]
		rakstitajs = csv.DictWriter(fails1, fieldnames=lauki,delimiter=",")
		rakstitajs.writeheader()
		for ieraksts in saraksts:
			rakstitajs.writerow(ieraksts)		
	with open("komponentes.csv","w") as fails1:
		lauki = ["Veids", "Razotajs", "Modelis", "Spec", "Cena"]
		rakstitajs = csv.DictWriter(fails1, fieldnames=lauki,delimiter=",")
		rakstitajs.writeheader()
		for ieraksts in saraksts:
			rakstitajs.writerow(ieraksts)	
	jdetala = ievade()
	jdetala.raksta("komponentes.csv")
def main():
	print("Labrīt!")
	while True:
		print ("1 - skatīt, 2 - pievienot, 3 - labot")
		v = input("Ievadi izvēli : ")
		if v == "1":
			lasa()
		elif v == "2":
			meginu = ievade()
			meginu.raksta("komponentes.csv")
		elif v == "3":
			num = int(input("Ievadi detaļas numuru: "))
			labot(num)
		else:
			break
	print("Jauku vakaru!")	

# Programma
main()
