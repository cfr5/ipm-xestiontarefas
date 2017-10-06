import gi
gi.require_version('Gtk', '3.0')
from datetime import datetime, date
from gi.repository import Gtk, GLib, GObject


class View():

	def __init__(self, controller):
		self._win = Gtk.Window(title="Práctica 1 -- IPM 17/18")
		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
		self._win.add(box)

		#Boton Salir
		button = Gtk.Button(label="Salir")
		button.connect('clicked', controller.on_button_salir_clicked)
		box.pack_end(button, True, True, 0)

		self.store = Gtk.ListStore(str, GObject.TYPE_PYOBJECT, bool)

		#Tree view
		self.tree = Gtk.TreeView(self.store)
		renderer = Gtk.CellRendererText()
		column = Gtk.TreeViewColumn("Tarea", renderer, text=0)
		self.tree.append_column(column)
		column.set_sort_column_id(0)
		renderer = Gtk.CellRendererText()
		column = Gtk.TreeViewColumn("Fecha", renderer)
		column.set_cell_data_func(renderer, controller.fecha_cell_data_func)
		self.tree.append_column(column)
		column.set_sort_column_id(1)
		self.store.set_sort_func(1, self.compare_fecha, None)
		renderer = Gtk.CellRendererToggle()
		column = Gtk.TreeViewColumn("Hecho", renderer, active=2)
		self.tree.append_column(column)
		box.pack_end(self.tree, True, True, 0)
		column.set_sort_column_id(2)

		####
		box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
		box.pack_start(box2, True, True, 0)

		#Boton anadir
		button = Gtk.Button(label="Añadir")
		button.connect('clicked', controller.on_button_añadir_clicked, self.tree)
		box2.pack_end(button, True, True, 0)

		#Boton eliminar
		button = Gtk.Button(label="Eliminar")
		button.connect('clicked', controller.on_button_eliminar_clicked, self.tree)
		box2.pack_end(button, True, True, 0)

		#Boton editar
		button = Gtk.Button(label="Editar")
		button.connect('clicked', controller.on_button_editar_clicked, self.tree)
		box2.pack_end(button, True, True, 0)




	def showWelcome(self):
		welcome = Gtk.Dialog("El mítico gestor de tareas",self._win, 0,
                     (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                          Gtk.STOCK_OK, Gtk.ResponseType.OK))
		vbox = Gtk.VBox(spacing = 10)
		welcome.get_content_area().add(vbox)

		etiqueta1 = Gtk.Label("Bienvenido !!!!!111!!!")

		etiqueta2 = Gtk.Label("(╯◕_◕)╯ (╯◕_◕)╯ ╰(◣﹏◢)╯ ╰(◕_◕╰) ╰(◕_◕╰)")
		vbox.pack_start(etiqueta1, True, True, 0)
		vbox.pack_start(etiqueta2, True, True, 0)
		welcome.show_all()
		respuesta = welcome.run()
		if respuesta == Gtk.ResponseType.OK:
			welcome.destroy()
			self._win.show_all()
		elif respuesta == Gtk.ResponseType.CANCEL:
			welcome.destroy()
			GLib.idle_add(Gtk.main_quit)


	def añadir_tarea_view(self, data):
		if data != None:
			self.tree.get_model().append(data)

	def editar_tarea_view(self, model, treeiter, data):
		if data != None:
			model.set(treeiter, 0, data[0])
			model.set(treeiter, 1, data[1])
			model.set(treeiter, 2, data[2])

	def run_dialog_añadir_editar(self,title, parent, data=None):
	    dialog = Gtk.Dialog(title, parent, Gtk.DialogFlags.DESTROY_WITH_PARENT, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK))
	    box = dialog.get_content_area()
	    grid = Gtk.Grid()
	    tareaEntry = Gtk.Entry()
	    fechaEntry = Gtk.Entry()
	    hechoCheckButton = Gtk.CheckButton("Hecho")
	    if data != None:
	        tareaEntry.set_text(data[0])
	        fechaEntry.set_text(data[1].strftime("%x"))
	        hechoCheckButton.set_active(data[2])
	    grid.attach(Gtk.Label("Tarea"), 0, 0, 1, 1)
	    grid.attach(tareaEntry, 1, 0, 1, 1)
	    grid.attach(Gtk.Label("Fecha"), 0, 1, 1, 1)
	    grid.attach(fechaEntry, 1, 1, 1, 1)
	    grid.attach(hechoCheckButton, 1, 2, 1, 1)
	    box.pack_start(grid, True, True, 0)
	    box.show_all()
	    response = dialog.run()
	    data = None
	    if response == Gtk.ResponseType.OK:
	        try:
	            data = [tareaEntry.get_text(), datetime.strptime(fechaEntry.get_text(), "%x"), hechoCheckButton.get_active()]
	        except ValueError:
	            pass
	    dialog.destroy()
	    return data

	def showSalir(self, widget):
		dialog = Gtk.MessageDialog(widget.get_toplevel(), 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "¿ Quieres detener esta acción ?")
		dialog.format_secondary_text("Si no la detienes, el programa terminará")
		dialog.run()
		dialog.destroy()
		Gtk.main_quit()

	def compare_fecha(self, model, treeiter1, treeiter2, user_data):
        	if model[treeiter1][1] < model[treeiter2][1]:
            		return -1
        	if model[treeiter1][1] > model[treeiter2][1]:
            		return 1
        	return 0
