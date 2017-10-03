from view import *
#from model import *

class Controller():

	def  __init__(self):
		#self.model = Model(self)
		
		self.view = View(self)
		self.doWelcome()


	def on_close (self,):
		Gtk.main_quit()

	def on_button_salir_clicked(self):
		self.view.showSalir()
		Gtk.main_quit()

		
	def doWelcome(self):
		respuesta = self.view.showWelcome()
		if respuesta == Gtk.ResponseType.OK:
			self.view.win.show_all()
		elif respuesta == Gtk.ResponseType.CANCEL:
			Gtk.main_quit()
