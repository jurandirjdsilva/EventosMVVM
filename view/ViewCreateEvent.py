from view import View
from view import ViewLogin
from viewModel import ViewModelCreateEvent
import datetime

class ViewCreateEvent (View.View):
    def __init__(self, root):

        self.controller = root
        self.viewModelList = []
        self.viewModel = ViewModelCreateEvent.ViewModelCreateEvent()
        self.viewModel.attach(self)
        pass
    def show(self):

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
            self.viewModel.CreateEvent(name, dt_start.__str__(), dt_end.__str__(), address)
        else :
            self.controller.show(ViewLogin.ViewLogin(self.controller))
            pass
