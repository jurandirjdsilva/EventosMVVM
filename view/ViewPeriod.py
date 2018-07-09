from view import View
from viewModel import ViewModelPeriod
class ViewPeriod (View.View):
    def __init__(self, controller, dtstart ,dtend):
        self.controller = controller
        self.viewModelList = []
        self.viewModel = ViewModelPeriod.ViewModelPeriod(dtstart, dtend)
        self.viewModel.attach(self)
        pass
    def show(self):
        self.update()
        print(self.state)
        pass