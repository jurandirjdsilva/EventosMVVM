from view import ViewMain

class Main():
    def __init__(self):
        self.viewStack = []
    def run(self):
        self.empilha(ViewMain.ViewMain()) 
        pass
    def empilha(self,view):
        self.viewStack.append(view)
        self.viewStack[-1].show()
        self.desempilha()
        pass
    def desempilha(self):
        self.viewStack.pop()
        pass






    
if __name__ == "__main__":
    main = Main()
    main.run()