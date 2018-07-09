from view import View
from viewModel import ViewModelEvent
class ViewEvent (View.View):
    def __init__(self, controller, id):
        self.id = id
        self.controller = controller
        self.viewModelList = []
        self.viewModel = ViewModelEvent.ViewModelEvent(self.id)
        self.viewModel.attach(self)
        pass
    def show(self):
        self.update()
        print(self.state)
        option = input(
            "0 para sair , 1 para editar o evento ")
        if option == '1':
            # colher dados do evento
            # chamar editevent na viewModelEvent

            pass
        elif option == '0':
            pass