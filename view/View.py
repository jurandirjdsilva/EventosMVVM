from viewModel import ViewModel

class View():
    state = None
    def __init__(self, controller ):

        self.root = controller
        self.viewModelList = []
        self.viewModel = ViewModel.ViewModel()
        self.viewModel.attach(self)
        pass


    def attach(self,viewModel):
        self.viewModelList.append(viewModel)
    def deatach(self,viewModel):
        self.viewModelList.remove(viewModel)

    def update(self):
        self.state = self.viewModel.getState()


    def show(self):

        print(self.state)
        pass
