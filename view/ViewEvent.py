from view import View
from view import ViewLogin
import datetime
from viewModel.ViewModelEvent import ViewModelEvent

class ViewEvent (View.View):
    def __init__(self, root, name):
        self.name = name
        self.root = root
        self.viewModelList = []
        self.viewModel = ViewModelEvent(name)
        self.viewModel.attach(self)
        self.event = self.viewModel.event
        pass

    def update(self):
        self.state = self.viewModel.get_state()
        self.event = self.viewModel.event

    def show(self):
        if self.event is not None :
            print(self.event)
            print('*********************************************')
            print('*                  {}                  *'.format(self.event.get_name()))
            print('*********************************************')
            print('*local : {}                  *'.format(self.event.get_address()))
            print('*de {} ate {}                 *'.format(self.event.get_start_date(), self.event.get_end_date()))
            print('*{}                  *'.format(self.event.get_description()))

            option = input("0 para retornar , 1 para editar o evento ")
            if option == '1':
                if (True):
                    # colher dados do evento
                    name = input("Nome do evento: ")
                    date_entry = input('Data de início (AAAA-MM-DD): ')
                    year, month, day = map(int, date_entry.split('-'))
                    dt_start = datetime.date(year, month, day)
                    date_entry = input('Data de término (AAAA-MM-DD): ')
                    year, month, day = map(int, date_entry.split('-'))
                    dt_end = datetime.date(year, month, day)
                    hr_start = None
                    hr_end = None
                    """
                    time_entry = input('Hora de inicio:(HH:MM:SS:00) ')
                    hour, minute, second, microsecond = (int, time_entry.split(':'))
                    hr_start = datetime.time(hour, minute, second, microsecond)

                    time_entry = input('Hora de término:(HH:MM:SS:00)  ')
                    hour, minute, second, microsecond = (int, time_entry.split(':'))
                    hr_end = datetime.time(hour, minute, second, microsecond)
                    """
                    address = input("Local: ")
                    description = input('Conteúdo do evento: ')
                    #  im = Image.open("imagemEvento.jpg")
                    self.viewModel.editEvent(name, dt_start, dt_end, address, hr_start, hr_end, description)
                else :
                    self.root.show(ViewLogin.ViewLogin(self.root))
                    pass

            elif option == '0':
                pass