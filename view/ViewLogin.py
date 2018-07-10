from view import View
from viewModel import ViewModelLogin
from getpass import getpass
from hashlib import md5 
class ViewLogin(View.View):
    def __init__(self, controller ):
        self.controller = controller
        self.viewModelList = []
        self.viewModel = ViewModelLogin.ViewModelLogin()
        self.viewModel.attach(self)
        pass

    pass
    def show(self):
        #para teste
        self.viewModel.createUser('ramon','ramon.jsa@gmail.com','ramon',md5('senha'.encode()).hexdigest())
        user = input("Usuario:")
        password = md5(getpass().encode()).hexdigest()
        self.viewModel.verify(user,password)
        print(user)
        print(password)
