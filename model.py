from datetime import datetime, date
from random import randint
import time

class Model():

	def __init__ (self, controller):
		self.list = []

		self.list.append(["Llevar coche al taller", date.today(), False])
		self.list.append(["Lavar el coche", date(2017, 8, 1), False])
		self.list.append(["Pagar el seguro", date(2017,1,1), False])
		self.list.append(["Arreglar mando garaje", date.today(), False])
		self.list.append(["Recoger ropa del tinte", date.today(), False])
		self.list.append(["Regalo cumpleaños Nico", date(2018,1,1), False])
		self.list.append(["Devolver libro a la biblioteca", date(2018,2,12), True])
		self.list.append(["Ordenar el congelador", date(2017,9,12), False])
		self.list.append(["Lavar las cortinas", date(2017,10,1), False])
		self.list.append(["Organizar el cajón de los mandos", date(2017,10,5), False])
		self.list.append(["Poner flores en las jardineras", date.today(), False])

	def insertar_lista(self, data):
		if data != None:
			if (type(data[1]) is datetime):
				self.list.append(data)
				


	def editar_valor_lista(self, nombre, data):
		if nombre != None:
				for sublist in self.list:
					if sublist[0] == nombre:
						sublist[0] = data[0]
						sublist[1] = data[1]
						sublist[1] = data[2]

	def eliminar_valor_lista(self, nombre):
		if nombre != None:
			for sublist in self.list:
				if sublist[0] == nombre:
					self.list.remove(sublist)

	def get_list(self):
		return self.list

	def server_sync(self, lista):
		lista2 = lista
		random = randint(0,10)
		time.sleep(random)
		return True


