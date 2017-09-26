import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, GObject

class View():

	def __init__(self, controller):

		win = Gtk.Window(title="Práctica 1 -- IPM 17/18")
		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
		win.add(box)

		button = Gtk.Button(label="Salir")
		button.connect('clicked', controller.on_button_salir_clicked)
		box.pack_end(button, True, True, 0)

		GLib.idle_add(self.showWelcome,win)


	def showWelcome(self,win):
		welcome = Gtk.Dialog("El mítico gestor de tareas", win, 0,
                     (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                          Gtk.STOCK_OK, Gtk.ResponseType.OK))
		vbox = Gtk.VBox(spacing = 10)
		welcome.get_content_area().add(vbox)

		etiqueta1 = Gtk.Label("Bienvenido !!!!!111!!!")

		etiqueta2 = Gtk.Label("(╯◕_◕)╯ (╯◕_◕)╯ ╰(◣﹏◢)╯ ╰(◕_◕╰) ╰(◕_◕╰)")
		vbox.pack_start(etiqueta1, True, True, 0)
		vbox.pack_start(etiqueta2, True, True, 0)
		welcome.show_all()

	def showSalir(self):
		dialog = Gtk.MessageDialog(widget.get_toplevel(), 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "¿ Quieres detener esta acción ?")
		dialog.format_secondary_text("Si no la detienes, el programa terminará")
		dialog.run()
		dialog.destroy()
