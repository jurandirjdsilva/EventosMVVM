from viewModel import ViewModel


class ViewModelEvent(ViewModel.ViewModel):
    def __init__(self, id):
        self.viewList = []
        self.id = id
        self.state = "estado evento " + id
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