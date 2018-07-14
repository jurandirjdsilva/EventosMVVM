from view import View
from view import ViewLogin

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
                    name = input ("nome")
                    date_entry = input('data do inicio no formato  AAAA-MM-DD')
                    year, month, day = map(int, date_entry.split('-'))
                    dt_start = datetime.date(year, month, day)
                    date_entry = input('data do fim no formato  AAAA-MM-DD')
                    year, month, day = map(int, date_entry.split('-'))
                    dt_end = datetime.date(year, month, day)
                    address  = input ("endereço")
                    # chamar editevent na viewModelEvent
                    # TODO
                    self.viewModel.editEvent(name, dt_start, dt_end, address)
                else :
                    self.root.show(ViewLogin.ViewLogin(self.root))
                    pass

            elif option == '0':
                pass