class ViewModel():
    def __init__(self):
        self.viewList = []

    def getState(self):
        pass
    def setState(self):
        pass
    
    def attach(self,view):
        self.viewList.append(view)
    def deatach(self,view):
        self.viewList.remove(view)
    def notify(self):
        for view in self.viewList :
            view.update(self)
    
