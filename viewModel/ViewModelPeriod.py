from viewModel import ViewModel


class ViewModelPeriod(ViewModel.ViewModel):
    def __init__(self, dtstart, dtend):
        self.viewList = []
        self.state = "estado periodo " + dtstart + " a " + dtend
