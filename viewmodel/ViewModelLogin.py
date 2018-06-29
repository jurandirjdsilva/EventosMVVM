from model import User
from model import Credential
from viewmodel import ViewModel


class ViewModelLogin(ViewModel.ViewModel):



    def createUser(self, name, email, user, password):
        self.user = User (name, email)
        self.credential = Credential(user,password)
        Credential.credentialList.append(self.credential)

    def verify(self,user,password):
        for c in Credential.credentialList:
            if c.user == user and c.password == password:
                return True
        pass
