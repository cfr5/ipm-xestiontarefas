from view import *
#from model import *

class Controller():

	def  __init__(self):
		#self.model = Model(self)
		
		self.view = View(self)
		cont = self.view.showWelcome()
		if cont:
			print("continuar")
		else:
			print("salir")
			#Gtk.main_quit()


	def on_close (self,):
		Gtk.main_quit()

	def on_button_salir_clicked(self):
		self.view.showSalir()
		Gtk.main_quit()

		
	
