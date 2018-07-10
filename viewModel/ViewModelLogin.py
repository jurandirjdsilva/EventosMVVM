from model import User
from model import Credential
from viewModel import ViewModel


class ViewModelLogin(ViewModel.ViewModel):



    def createUser(self, name, email, user, password):
        self.user = User.User (name, email)
        self.credential = Credential.Credential('1',user,password)
        Credential.credentialList.append(self.credential)

    def verify(self,user,password):
        for c in Credential.credentialList:
            if c.user == user and c.password == password:
                print("logou !!!")
                global loged
                loged = True
                return True
        return False
