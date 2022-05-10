# (C) Grupa VP3, 2022

# Moduļi
import PySimpleGUI as sg
sg.theme('DarkAmber')
import csv

# Klases
class Izskats:
	# Jāpastudē https://github.com/PySimpleGUI/PySimpleGUI/issues/775#issuecomment-751258544
	def __init__(self, logs, izkartojums):
		# vispārējie
		self.logs = logs
		self.izkartojums = izkartojums

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
			if self.veids != "" or self.razotajs != "" or self.modelis != "" or self.spec != "" or self.cena != "":
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

class Fails:
	def __init__ (self):
		pass
	def lasa(self,faila_vards):
		with open(faila_vards, "r") as fails:
			lasitajs = csv.DictReader(fails)
			skaititajs = 1
			for rinda in lasitajs:
				print(skaititajs,"=",rinda)
				skaititajs += 1
	def labot(self,faila_vards,nr):
		saraksts = []
		with open(faila_vards, "r") as fails:
			lasitajs = csv.DictReader(fails)
			for rinda in lasitajs:
				saraksts.append(rinda)
			print("Labojamā informācija:")
			print(saraksts[nr-1])
			saraksts.pop(nr-1)
			#print(saraksts)
		with open(faila_vards,"w") as fails1:
			lauki = ["Veids", "Razotajs", "Modelis", "Spec", "Cena"]
			rakstitajs = csv.DictWriter(fails1, fieldnames=lauki, delimiter=",")
			rakstitajs.writeheader()
			for ieraksts in saraksts:
				rakstitajs.writerow(ieraksts)		
		jdetala = ievade()
		jdetala.raksta("komponentes.csv")
		
# Metodes
	
def ievade():
	detala = Komponente("","","","","")
	izkartojums = [  [sg.Text('Komponentes')],
				[sg.Text('Veids'), sg.InputText()],
				[sg.Text('Ražotājs'), sg.InputText()],
				[sg.Text('Modelis'), sg.InputText()],
				[sg.Text('Specifikācija'), sg.InputText()],
				[sg.Text('Cena'), sg.InputText()],
				[sg.Button('Ok'), sg.Button('Exit')] ]	
	logs = sg.Window('Komponenšu logs', izkartojums)
	while True:
		notikums, vertibas = logs.read()
		if notikums == sg.WIN_CLOSED or notikums == 'Exit':
			break
		sg.popup('Tu ievadīji', vertibas)  
	#print ("Veids", "Razotajs", "Modelis", "Spec", "Cena")
		veids = vertibas[0]
		razotajs = vertibas[1]
		modelis = vertibas[2]
		spec = vertibas[3]
		cena = vertibas[4]
		detala = Komponente(veids,razotajs,modelis,spec,cena)
	logs.close()
	return detala

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

def mainconsole():
	print("Labrīt!")
	while True:
		print ("1 - skatīt, 2 - pievienot, 3 - labot")
		v = input("Ievadi izvēli : ")
		if v == "1":
			fails = Fails()
			fails.lasa("komponentes.csv")
		elif v == "2":
			detala = ievade()
			detala.raksta("komponentes.csv")
		elif v == "3":
			num = int(input("Ievadi detaļas numuru: "))
			fails = Fails()
			fails.labot("komponentes.csv",num)
		else:
			break
	print("Jauku vakaru!")	
def main():
	# Uzskaita visus objektus logā: teksta uzrakstus, ievades logu, pogas
	p_izkartojums = [  [sg.Text('Izvēlies, ko darīsi:')],
				   [sg.Button('Skatīt'), sg.Button('Ievadīt'), sg.Button('Labot'), sg.Button('Exit')] ]
	# Izveido logu
	s_logs = sg.Window('Galvenā izvēlne', p_izkartojums)
	# Cikls apstrādā notikumus un iegūst ievades vērtības
	while True:
		notik, vert = s_logs.read()
		if notik == sg.WIN_CLOSED or notik == 'Exit':
			break
		if notik == 'Skatīt':
			fails = Fails()
			fails.lasa("komponentes.csv")
		if notik == 'Ievadīt':
			detala = ievade()
			detala.raksta("komponentes.csv")
		if notik == 'Labot':
			num = int(input("Ievadi detaļas numuru: "))
			fails = Fails()
			fails.labot("komponentes.csv",num)
	s_logs.close()	
# Programma
main()
