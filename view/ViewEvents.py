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
        print(self.state)
        pass