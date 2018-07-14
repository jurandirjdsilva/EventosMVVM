from viewModel import ViewModel
from model.Event import Event
from model.DAO import EventDAO

class ViewModelEvent(ViewModel.ViewModel):
    def __init__(self, name):
        self.viewList = []
        self.event= EventDAO.select_event(name)
        self.state = self.event


    def editEvent (self,name,dt_start,dt_end,address):
        self.name = name
        self.dt_start = dt_start
        self.dt_end = dt_end
        self.address=address
        self.state="estado evento "+ self.id + self.name+self.dt_start+self.dt_end+self.address
        # atualiza modelo
        self.notify()
        pass
    def IsLoggedIn(self):
        #busca no modelo se esta logado
        if 'loged' in globals():
            print('loged esta entre os globais')
            global loged
            if loged == True :
                return True
            else:
                return False
        else:
            return False