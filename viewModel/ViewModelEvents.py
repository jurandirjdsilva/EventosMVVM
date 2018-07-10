from viewModel import ViewModel


class ViewModelEvents(ViewModel.ViewModel):
    def __init__(self):
        self.viewList = []
        self.state = None

    def get_events(self):
