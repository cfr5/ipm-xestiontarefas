from view import *
#from model import *

class Controller():

	def  __init__(self):
		#self.model = Model(self)

		self.view = View(self)
		self.view.showWelcome()



	def on_close (self,):
		Gtk.main_quit()

	def on_button_salir_clicked(widget):
		self.view.showSalir(widget)
