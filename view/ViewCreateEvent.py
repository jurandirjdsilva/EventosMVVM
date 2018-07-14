from view import View
from view import ViewLogin
from viewModel.ViewModelCreateEvent import ViewModelCreateEvent
import datetime

class ViewCreateEvent(View.View):
    def __init__(self, root):

        self.root = root
        self.viewModelList = []
        self.viewModel = ViewModelCreateEvent()
        self.viewModel.attach(self)

    def show(self):
        # criei uma funcao de teste para facilitar , so imprime teste
        self.viewModel.teste()
        if (True):
            # colher dados do evento
            name = input ("Nome do evento: ")

            date_entry = input('Data de início (AAAA-MM-DD): ')
            year, month, day = map(int, date_entry.split('-'))
            dt_start = datetime.date(year, month, day)

            date_entry = input('Data de término (AAAA-MM-DD): ')
            year, month, day = map(int, date_entry.split('-'))
            dt_end = datetime.date(year, month, day)
            #TODO fix it
            hr_start ='12:12:12:00'
            hr_end = '12:12:12:00'

            '''
            time_entry = input('Hora de inicio: ')
            hour, minute, second, microsecond = (int, date_entry.split(':'))
            hr_start = datetime.time(hour, minute, second, microsecond)

            time_entry = input('Hora de término: ')
            hour, minute, second, microsecond = (int, date_entry.split(':'))
            hr_end = datetime.time(hour, minute, second, microsecond)
            '''

            address  = input ("Local: ")

            description = input('Conteúdo do evento: ')

            #  im = Image.open("imagemEvento.jpg")
            self.viewModel.CreateEvent(name, dt_start, dt_end, address, hr_start, hr_end, description)
            #self.viewModel.createEvent(name, dt_start, dt_end,address, hr_start, hr_end, description)
        else :
            self.root.show(ViewLogin.ViewLogin(self.root))
pass
