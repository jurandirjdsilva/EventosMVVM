from view import View
from view import ViewLogin
from viewModel import ViewModelCreateEvent
import datetime

class ViewCreateEvent (View.View):
    def _init_(self, root):

        self.root = root
        self.viewModelList = []
        self.viewModel = ViewModelCreateEvent.ViewModelCreateEvent()
        self.viewModel.attach(self)
        pass
    def show(self):

        if (self.viewModel.IsLoggedIn()):
            # colher dados do evento
            name = input ("Nome do evento: ")

            date_entry = input('Data de início (AAAA-MM-DD): ')
            year, month, day = map(int, date_entry.split('-'))
            dt_start = datetime.date(year, month, day)

            date_entry = input('Data de término (AAAA-MM-DD): ')
            year, month, day = map(int, date_entry.split('-'))
            dt_end = datetime.date(year, month, day)

            time_entry = input('Hora de inicio: ')
            hour, minute, second, microsecond = (int, date_entry.split(':'))
            hr_start = datetime.time(hour, minute, second, microsecond)

            time_entry = input('Hora de término: ')
            hour, minute, second, microsecond = (int, date_entry.split(':'))
            hr_end = datetime.time(hour, minute, second, microsecond)

            address  = input ("Local: ")

            description = input('Conteúdo do evento: ')

            #  im = Image.open("imagemEvento.jpg")

            self.viewModel.CreateEvent(name, dt_start._str(), dt_end.str_(), hr_start._str(), hr_end._str(), address, description._str())
        else :
            self.root.show(ViewLogin.ViewLogin(self.root))
pass
