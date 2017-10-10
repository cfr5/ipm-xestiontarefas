from datetime import datetime, date

class Model():

	def __init__ (self, controller):
		self.list = []

		self.list.append(["Llevar coche al taller", date.today(), False])
		self.list.append(["Lavar el coche", date(2017, 8, 1), False])
		self.list.append(["Pagar el seguro", date(2017,1,1), False])
		self.list.append(["Arreglar mando garaje", date.today(), False])

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
