from view import View
from view import ViewLogin
from viewModel import ViewModelCreateEvent
class ViewCreateEvent (View.View):
    def __init__(self, controller):

        self.controller = controller
        self.viewModelList = []
        self.viewModel = ViewModelCreateEvent.ViewModelCreateEvent()
        self.viewModel.attach(self)
        pass
    def show(self):

        print(self.viewModel.IsLoggedIn)
        if (self.viewModel.IsLoggedIn):
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
            self.viewModel.CreateEvent(name, dt_start, dt_end, address)
        else :
            self.controller.show(ViewLogin.ViewLogin(self.controller))
            pass
