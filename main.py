from view import ViewMain
from view import ViewEvents

import datetime

class Root:
    def __init__(self):

        pass
    def run(self):
        self.show(ViewEvents.ViewEvents(self))
        self.show(ViewMain.ViewMain(self))
        pass
    def show (self, view):
            view.show()

if __name__ == "__main__":


    root = Root()
    root.run()
