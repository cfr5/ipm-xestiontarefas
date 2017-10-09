from view import *
from model import *

class Controller():

    def  __init__(self):
        self.model = Model(self)
        self.view = View(self)
        self.initialice_list(self.model.list, self.view.store)
        self.view.showWelcome()

    def initialice_list(self, lista, store):
        if lista != None:
            for sublist in lista:
                self.view.store.append(sublist)


    def on_button_salir_clicked(self, widget):
        self.view.showSalir(widget)


    def on_button_añadir_clicked(self, widget):
        data = self.view.run_dialog_añadir_editar("Añadir tarea", widget.get_toplevel())
        self.model.insertar_lista(data)
        self.view.añadir_tarea_view(data)


    def on_button_editar_clicked(self, widget):
        model1, treeiter = self.view.obtener_seleccion()
        if treeiter != None:
            data = self.view.run_dialog_añadir_editar("Editar tarea", widget.get_toplevel(), model1[treeiter])
            self.view.editar_tarea_view(model1, treeiter, data)
            self.model.editar_valor_lista(self.view.store[treeiter][0], data)


    def on_button_eliminar_clicked(self, widget):
        model1, treeiter = self.view.obtener_seleccion()
        if treeiter != None:
            self.model.eliminar_valor_lista(self.view.store[treeiter][0])
            self.view.eliminar_tarea_view(model1, treeiter)
            



