from view import *
from model import *

class Controller():

    def  __init__(self):
        self.model = Model(self)
        self.view = View(self)
        self.initialice_list(self.model.get_list(), self.view.get_store())
        self.view.showWelcome()

    def initialice_list(self, lista, store):
        if lista != None:
            for sublist in lista:
                self.view.store.append(sublist)

    def on_button_salir_clicked(self, widget):
        self.view.showSalir(widget)


    def on_button_añadir_clicked(self, widget):
        data = self.view.añadir_tarea_view(widget)
        self.model.insertar_lista(data)


    def on_button_editar_clicked(self, widget):
        dataold, datanew = self.view.editar_tarea_view(widget)
        if dataold != None and datanew != None:
            self.model.editar_valor_lista(dataold, datanew)

    def on_button_eliminar_clicked(self, widget):
        data = self.view.eliminar_tarea_view(widget)
        self.model.eliminar_valor_lista(data)     



