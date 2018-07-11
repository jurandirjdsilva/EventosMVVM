from view import View
from view import ViewLogin
from viewModel import ViewModelEvent
class ViewEvent (View.View):
    def __init__(self, root, id):
        self.id = id
        self.root = root
        self.viewModelList = []
        self.viewModel = ViewModelEvent.ViewModelEvent(self.id)
        self.viewModel.attach(self)
        pass
    def show(self):
        self.update()
        print(self.state)
        option = input("0 para sair , 1 para editar o evento ")
        if option == '1':
            print(self.viewModel.IsLoggedIn())
            if (self.viewModel.IsLoggedIn()):
                # colher dados do evento
                name = input ("nome")
                date_entry = input('data do inicio no formato  AAAA-MM-DD')
                year, month, day = map(int, date_entry.split('-'))
                dt_start = datetime.date(year, month, day)
                date_entry = input('data do fim no formato  AAAA-MM-DD')
                year, month, day = map(int, date_entry.split('-'))
                dt_end = datetime.date(year, month, day)
                address  = input ("endereço")
                # chamar editevent na viewModelEvent
                self.viewModel.editEvent(name, dt_start, dt_end, address)
            else :
                self.controller.show(ViewLogin.ViewLogin(self.controller))
                pass

        elif option == '0':
            pass