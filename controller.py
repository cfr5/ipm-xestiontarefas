from view import *
from model import *
import threading

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


    def on_button_anadir_clicked(self, widget):
        data = self.view.anadir_tarea_view(widget)
        self.model.insertar_lista(data)
        threading.Thread(target=self.call_server_sync, args=[self.model.get_list()], daemon=True).start()


    def on_button_editar_clicked(self, widget):
        dataold, datanew = self.view.editar_tarea_view(widget)
        if dataold != None and datanew != None:
            self.model.editar_valor_lista(dataold, datanew)
            threading.Thread(target=self.call_server_sync, args=[self.model.get_list()], daemon=True).start()

    def on_button_eliminar_clicked(self, widget):
        data = self.view.eliminar_tarea_view(widget)
        self.model.eliminar_valor_lista(data)   
        threading.Thread(target=self.call_server_sync, args=[self.model.get_list()], daemon=True).start() 
         

    def on_button_ayuda_clicked(self, widget):
        self.view.showHelp(widget)
    
    def on_button_acerca_de_clicked(self, widget):
        self.view.showAbout(widget) 

    def on_button_forzar_clicked(self, widget):
        threading.Thread(target=self.call_server_sync, args=[self.model.get_list()], daemon=True).start() 

    def call_server_sync(self, lista):
        self.view.start_spinner()
        resp=self.model.server_sync(lista)
        if resp:
            self.view.stop_spinner()
        else:
            self.view.error_sync()



