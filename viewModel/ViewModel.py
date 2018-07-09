class ViewModel():
    def __init__(self):
        self.viewList = []
        self.state = "teste estado"

    def getState(self):
        return self.state

    def setState(self):
        # busca no modelo
        pass

    def attach(self, view):
        self.view = view
        self.viewList.append(view)

    def deatach(self, view):
        self.viewList.remove(view)

    def notify(self):
        self.view.update()
        for view in self.viewList:
            view.update(self)
