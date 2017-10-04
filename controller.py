from view import *
#from model import *

class Controller():

	def  __init__(self):
		#self.model = Model(self)

		self.view = View(self)
		self.view.showWelcome()



	def on_close (self):
		Gtk.main_quit()

	def on_button_salir_clicked(self, widget):
		self.view.showSalir(widget)


	def on_button_añadir_clicked(self, widget, tree):
		data = self.view.run_dialog_añadir_editar("Añadir tarea", widget.get_toplevel())
		if data != None:
			self.view.tree.get_model().append(data)


	def on_button_editar_clicked(self, widget, tree):
		selection = self.view.tree.get_selection()
		model, treeiter = selection.get_selected()
		if treeiter != None:
			data = self.view.run_dialog_añadir_editar("Editar tarea", widget.get_toplevel(), model[treeiter])
			if data != None:
				model.set(treeiter, 0, data[0])
				model.set(treeiter, 1, data[1])
				model.set(treeiter, 2, data[2])


	def on_button_eliminar_clicked(self, widget, tree):
	    selection = self.view.tree.get_selection()
	    model, treeiter = selection.get_selected()
	    if treeiter != None:
	        model.remove(treeiter)

	def fecha_cell_data_func(self, column, renderer, model, treeiter, data):
	    fecha = model[treeiter][1]
	    renderer.set_property('text', fecha.strftime("%x"))


	def compare_fecha(self, model, treeiter1, treeiter2, user_data):
	    if model[treeiter1][1] < model[treeiter2][1]:
	        return -1
	    if model[treeiter1][1] > model[treeiter2][1]:
	        return 1
	    return 0
