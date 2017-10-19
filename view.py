import gi
import locale
gi.require_version('Gtk', '3.0')
from datetime import datetime, date, time
from gi.repository import Gtk, Gdk, GLib, GObject


class View():

	def __init__(self, controller):
		self._win = Gtk.Window(title="Práctica 1 -- IPM 17/18")
		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
		self._win.add(box)

		menu = Gtk.MenuBar()		

		self.store = Gtk.ListStore(str, GObject.TYPE_PYOBJECT, bool)

		#Tree view
		self.tree = Gtk.TreeView(self.store)
		renderer = Gtk.CellRendererText()
		column = Gtk.TreeViewColumn("Tarea", renderer, text=0)
		self.tree.append_column(column)
		column.set_sort_column_id(0)
		renderer = Gtk.CellRendererText()
		column = Gtk.TreeViewColumn("Fecha", renderer)
		column.set_cell_data_func(renderer, self.fecha_cell_data_func)
		self.tree.append_column(column)
		column.set_sort_column_id(1)
		self.store.set_sort_func(1, self.compare_fecha, None)
		renderer = Gtk.CellRendererToggle()
		column = Gtk.TreeViewColumn("Hecho", renderer, active=2)
		self.tree.append_column(column)
		box.pack_end(self.tree, True, True, 0)
		column.set_sort_column_id(2)

		filemenu = Gtk.Menu()
		filem = Gtk.MenuItem("Archivo")
		filem.set_submenu(filemenu)
		
		editmenu = Gtk.Menu()
		editm = Gtk.MenuItem("Editar")
		editm.set_submenu(editmenu)

		helpmenu = Gtk.Menu()
		helpm = Gtk.MenuItem("Ayuda")
		helpm.set_submenu(helpmenu)

		####
		box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
		box.pack_start(box2, True, True, 0)

		#Boton ayuda
		button = Gtk.Button(label="Ayuda")
		button.connect('clicked', controller.on_button_ayuda_clicked)
		box2.pack_end(button, True, True, 0)
		
		ayuda = Gtk.MenuItem("Ayuda  F1")
		ayuda.connect("activate", controller.on_button_ayuda_clicked)
		helpmenu.append(ayuda)	
	
		#Boton eliminar
		button = Gtk.Button(label="Eliminar")
		button.connect('clicked', controller.on_button_eliminar_clicked)
		box2.pack_end(button, True, True, 0)

		eliminar = Gtk.MenuItem("Eliminar tarea")
		eliminar.connect("activate", controller.on_button_eliminar_clicked)
		editmenu.append(eliminar)

		#Boton editar
		button = Gtk.Button(label="Editar")
		button.connect('clicked', controller.on_button_editar_clicked)
		box2.pack_end(button, True, True, 0)

		editar = Gtk.MenuItem("Editar tarea")
		editar.connect("activate", controller.on_button_editar_clicked)
		editmenu.append(editar)

		#Boton anadir
		button = Gtk.Button(label="Añadir")
		button.connect('clicked', controller.on_button_añadir_clicked)
		box2.pack_end(button, True, True, 0)

		anadir = Gtk.MenuItem("Añadir tarea")
		anadir.connect("activate", controller.on_button_añadir_clicked)
		filemenu.append(anadir)

			

		about = Gtk.MenuItem("Acerca de")
		about.connect("activate", controller.on_button_acerca_de_clicked)
		helpmenu.append(about)

		######

		salir = Gtk.MenuItem("Salir")
		salir.connect("activate", controller.on_button_salir_clicked)
		filemenu.append(salir)

		menu.append(filem)
		menu.append(editm)
		menu.append(helpm)
		box.pack_start(menu, False, False, 0)


		self._win.connect('delete-event', self.on_close)
		
		self._win.connect("key-press-event",self._key_press_event,controller)

	def _key_press_event(self,widget,event,controller):
		state = event.state
		keyval = event.keyval
		keyval_name = Gdk.keyval_name(keyval)
		ctrl = (state & Gdk.ModifierType.CONTROL_MASK)
		if (ctrl and keyval_name == 'Delete'):
			controller.on_button_eliminar_clicked(widget)
		elif ((ctrl and keyval_name == 'e') | (keyval_name == 'Return')):
			controller.on_button_editar_clicked(widget)
		elif (ctrl and keyval_name == 'n'):
			controller.on_button_añadir_clicked(widget)
		elif (ctrl and keyval_name == 'q'):
			controller.on_button_salir_clicked(widget)
		elif (keyval_name == 'F1'):
			controller.on_button_ayuda_clicked(widget)
		else:
			return False
		return True

	def showWelcome(self):
		self._win.show_all()

	def fecha_cell_data_func(self, column, renderer, model, treeiter, data):
		fecha = model[treeiter][1]
		renderer.set_property('text', fecha.strftime("%x"))

	def dialog_exception_date(self, widget):
		dialog = Gtk.MessageDialog(widget.get_toplevel(), 0, Gtk.MessageType.INFO, 
				(Gtk.STOCK_OK, Gtk.ResponseType.OK), " Formato de fecha incorrecta")
		formatoFecha = locale.nl_langinfo(locale.D_FMT)
		dialog.format_secondary_text("El formato debe ser : Ej " + datetime.now().strftime(formatoFecha))
		dialog.run()
		dialog.destroy()

	def dialog_exception_selection(self, widget):
		dialog = Gtk.MessageDialog(widget.get_toplevel(), 0, Gtk.MessageType.INFO, 
				(Gtk.STOCK_OK, Gtk.ResponseType.OK), "Para realizar la acción, seleccione una tarea")
		dialog.run()
		dialog.destroy()

	def alert_edit_add(self, widget, title):
		if title == "Añadir tarea":
			tmp = "añadido"
		else: tmp = "actualizado"
		dialog = Gtk.MessageDialog(widget.get_toplevel(), 0, Gtk.MessageType.INFO, 
				(Gtk.STOCK_OK, Gtk.ResponseType.OK), "La tarea se ha "+ tmp + " correctamente")
		dialog.run()
		dialog.destroy()

	def obtener_seleccion(self):
		selection = self.tree.get_selection()
		model, treeiter = selection.get_selected()
		return model, treeiter


	def añadir_tarea_view(self, widget):
		data = self.run_dialog_añadir_editar("Añadir tarea", widget.get_toplevel())
		if data != None:
			self.tree.get_model().append(data)
			return data

	def editar_tarea_view(self, widget):
		model, treeiter = self.obtener_seleccion()
		data = None
		dataold = None
		if treeiter != None:
			data = self.run_dialog_añadir_editar("Editar tarea", widget.get_toplevel(), model[treeiter])
			dataold = self.store[treeiter][0]			
			if data != None and dataold != None:
				model.set(treeiter, 0, data[0])
				model.set(treeiter, 1, data[1])
				model.set(treeiter, 2, data[2])	
		else:
			self.dialog_exception_selection(widget)
		return dataold, data

	def eliminar_tarea_view(self, widget):
		model, treeiter = self.obtener_seleccion()
		data = None
		if treeiter != None:
			data = self.store[treeiter][0]
			model.remove(treeiter)
		else:
			self.dialog_exception_selection(widget)
		return data

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
	    grid.attach(Gtk.Label("Tarea  "), 0, 0, 1, 1)
	    grid.attach(tareaEntry, 1, 0, 1, 1)
	    grid.attach(Gtk.Label("Fecha  "), 0, 1, 1, 1)
	    grid.attach(fechaEntry, 1, 1, 1, 1)
	    grid.attach(hechoCheckButton, 1, 2, 1, 1)
	    box.pack_start(grid, True, True, 0)
	    box.show_all()
	    response = dialog.run()
	    data = None
	    if response == Gtk.ResponseType.OK:
	        try:
	            data = [tareaEntry.get_text(), datetime.strptime(fechaEntry.get_text(), "%x"), hechoCheckButton.get_active()]
	            self.alert_edit_add(parent.get_toplevel(), title)
	        except ValueError:
	            self.dialog_exception_date(parent.get_toplevel())
	    dialog.destroy()
	    return data


	def showSalir(self, widget):
		dialog = Gtk.MessageDialog(widget.get_toplevel(), 0, Gtk.MessageType.INFO, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                          Gtk.STOCK_OK, Gtk.ResponseType.OK), "¿ Quieres detener esta acción ?")
		dialog.format_secondary_text("Si no la detienes, el programa terminará")
		respuesta = dialog.run()
		if respuesta == Gtk.ResponseType.OK:
			dialog.destroy()
			Gtk.main_quit()
		elif respuesta == Gtk.ResponseType.CANCEL:
			dialog.destroy()
	
	def showHelp(self, widget):
		dialog = Gtk.MessageDialog(widget.get_toplevel(), 0, Gtk.MessageType.INFO, (Gtk.STOCK_OK, Gtk.ResponseType.OK), "¿Necesitas Ayuda?")
		dialog.format_secondary_text("Añadir:  Ctrl+N\n"+"Delete:  Ctrl+Supr\n"+"Editar:   Ctrl+E or Enter\n"+"Salir:       Ctrl+Q\n")
		respuesta = dialog.run()
		if respuesta == Gtk.ResponseType.OK:
			dialog.destroy()

	def showAbout(self, widget):
		dialog = Gtk.MessageDialog(widget.get_toplevel(), 0, Gtk.MessageType.INFO, (Gtk.STOCK_OK, Gtk.ResponseType.OK), "Acerca de IPM")
		dialog.format_secondary_text("Creadores:  Santiago Álvarez Fernandez y Carlos Franco Romero\n"+"Copyright © 2017 - IPM group\n")
		respuesta = dialog.run()
		if respuesta == Gtk.ResponseType.OK:
			dialog.destroy()

	def on_close(self, widget, *data):
		dialog = Gtk.MessageDialog(widget.get_toplevel(), 0, Gtk.MessageType.INFO, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                          Gtk.STOCK_OK, Gtk.ResponseType.OK), "¿ Quieres detener esta acción ?")
		dialog.format_secondary_text("Si no la detienes, el programa terminará")
		respuesta = dialog.run()
		if respuesta == Gtk.ResponseType.OK:
			dialog.destroy()
			Gtk.main_quit()
		elif respuesta == Gtk.ResponseType.CANCEL:
			dialog.destroy()
			return True
	

	def compare_fecha(self, model, treeiter1, treeiter2, user_data):
        	if model[treeiter1][1] < model[treeiter2][1]:
            		return -1
        	if model[treeiter1][1] > model[treeiter2][1]:
            		return 1
        	return 0

	def get_store(self):
		return self.store



