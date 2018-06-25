class View():
    def __init__(self):
        self.viewModelList = []
        pass

    def attach(self,viewModel):
        self.viewModelList.append(viewModel)
    def deatach(self,viewModel):
        self.viewModelList.remove(viewModel)

    def show(self):
        pass
    def update(self):
        pass