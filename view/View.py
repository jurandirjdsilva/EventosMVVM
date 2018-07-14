from viewModel import ViewModel

class View():
    state = None
    viewModel = None
    viewModelList = []
    def __init__(self, root):

        self.root = root
        self.viewModel = ViewModel.ViewModel()
        self.viewModel.attach(self)


    def attach(self,viewModel):
        self.viewModelList.append(viewModel)
    def deatach(self,viewModel):
        self.viewModelList.remove(viewModel)

    def update(self):
        self.state = self.viewModel.get_state()


    def show(self):

        print(self.state)