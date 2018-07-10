from viewModel import ViewModel


class ViewModelEvents(ViewModel.ViewModel):
    def __init__(self):
        self.viewList = []
        self.state = None

    def get_events(self):


    def find_Open_events(self):
        #TODO  busca no modelo

        self.notify()

    def find_period_events(self, dt_start, dt_end):
        # TODO  busca no modelo

        self.notify()