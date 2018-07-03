from viewmodel import ViewModel
class View():
    def __init__(self):
        self.viewModelList = []
        self.viewModel = ViewModel.ViewModel()
        pass

    def attach(self,viewModel):
        self.viewModelList.append(viewModel)
    def deatach(self,viewModel):
        self.viewModelList.remove(viewModel)

    def update(self):
        self.state = self.viewModel.getState()
        pass
    def show(self):
        self.update()
        print(self.state)
        pass