from view import View
from viewModel.ViewModelEvents import ViewModelEvents

class ViewEvents (View.View):
    def __init__(self, controller):
        self.controller = controller
        self.viewModelList = []
        self.viewModel = ViewModelEvents()
        self.viewModel.attach(self)
        pass

    def show(self):
        self.update()
        print('*********************************************')
        print('*                  Eventos                  *')
        print('*********************************************')

    def update(self):
        self.state = self.viewModel.getState()
        self.events = self.viewModel.
        print(self.state)
        pass

    def find_Open_events (self):
        self.viewModel.find_Open_events()
        pass

    def find_period_events(self,dt_start,dt_end):