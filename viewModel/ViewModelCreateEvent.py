from viewModel import ViewModel


class ViewModelCreateEvent(ViewModel.ViewModel):
    def __init__(self):
        self.viewList = []
        self.state = "estado novo evento" + id

    def CreateEvent(self, name, dt_start, dt_end, address):
        self.name = name
        self.dt_start = dt_start
        self.dt_end = dt_end
        self.address = address
        self.state = "estado evento " + self.id + self.name + self.dt_start + self.dt_end + self.address

        # atualiza modelo

        self.notify()
        pass

    def IsLoggedIn(self):

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
