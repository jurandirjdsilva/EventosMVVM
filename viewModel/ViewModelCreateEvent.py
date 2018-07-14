from viewModel import ViewModel
from model.Event import Event
from viewModel.ViewModel import ViewModel
from model.DAO import EventDAO

class ViewModelCreateEvent(ViewModel):
    def __init__(self):
        self.state = "estado novo evento"

    @property
    def teste(self):
        print("teste")

    def CreateEvent(self, name, dt_start, dt_end, address, hr_start=None, hr_end=None, description = None):

        event = Event(name,address,dt_start,dt_end,hr_start,hr_end,description)

        print(event)
        EventDAO.save_event(event)
        # atualiza modelo

        self.notify()
        pass

    @property
    def IsLoggedIn(self):
        return True # temporario
        # TODO   buscar no modelo se esta logado
        # FIXME
        if 'loged' in globals():
            print('loged esta entre os globais')
            global loged
            if loged == True:
                return True
            else:
                return False
        else:
            return False
