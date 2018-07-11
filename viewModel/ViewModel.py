class ViewModel():
    viewList = []
    state = None
    def __init__(self):

        self.state="teste estado"
        
    def get_state(self):
        return self.state
    
        
    def setState(self):
        pass
    
    def attach(self, view):
        self.viewList.append(view)
    def deatach(self,view):
        self.viewList.remove(view)
        
    def notify(self):
        for view in self.viewList :
            view.update()
    
