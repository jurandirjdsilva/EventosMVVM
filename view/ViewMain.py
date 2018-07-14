from view import View
from viewModel import ViewModelMain
from view import ViewEvents

from view import ViewEvent
from view import ViewCreateEvent

from threading import Thread

import datetime




class ViewMain(View.View):
    def __init__(self, root = None):
        self.root = root
        self.viewModelList = []
        self.viewModel = ViewModelMain.ViewModelMain()
        self.viewModel.attach(self)
        pass
    def show(self):

        option = input(
            "0 para sair , 1 para exibir um evento especifico, 2 para mostrar os eventos de um periodo e 3 para cadastrar eventos")
        if option == '1':
            print ("para exibir um evento especifico")
            nome = input("digite o nome do evento")

            self.root.show(ViewEvent.ViewEvent(self.root, nome))
            pass
        elif option == '2':
            print("para mostrar os eventos de um periodo ")
            date_entry = input('Digite a data inicial no formato  AAAA-MM-DD')
            year, month, day = map(int, date_entry.split('-'))
            dt_start = datetime.date(year, month, day)
            date_entry = input('Digite a data final no formato  AAAA-MM-DD')
            year, month, day = map(int, date_entry.split('-'))
            dt_end = datetime.date(year, month, day)


            self.root.show(ViewEvents.ViewEvents(self.root))

            pass
        elif option == '3':
            self.root.show(ViewCreateEvent.ViewCreateEvent(self.root))

        elif option == '0':
            print ("sair do programa")
            quit(0)
        self.root.show(self)

