from model import User

from viewmodel import ViewModel


class ViewModelLogin(ViewModel.ViewModel):



    def createUser(self, name, email, user, password):
        self.user = User(name, email)
        pass

    def verify():
        pass
