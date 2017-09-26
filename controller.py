from view import *
#from model import *

class Controller():

	def  __init__(self):
		#self.model = Model(self)
		self.view = View(self)
	def on_close (self, w):
		Gtk.main_quit()

	def on_button_salir_clicked(self):
		self.view.showSalir()
		Gtk.main_quit()

	def welcome(self):
		self.view.showWelcome()
		respuesta = welcome.run()

		if respuesta == Gtk.ResponseType.OK:
			welcome.destroy()
			self.view.win.show_all()
		elif respuesta == Gtk.ResponseType.CANCEL:
			welcome.destroy()
			Gtk.main_quit()
