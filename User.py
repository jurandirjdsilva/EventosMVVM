class User ():
    def __init__(self,nome,user,pass):
        self.name = name
        self.user = user 
        self.pass = pass
    def setName(self,name):
        self.name = name
    def setUser(self,user):
        self.user = user
    def setSenha(self,pass):
        self.pass = pass
    def getNome(self):
        return self.nome
    def getUser(self):
        return self.user
    
    def validate(self,user,pass):
        if self.user==user and self.pass==pass:
            return True
        else : 
            return False
        
def main():
    user = User("ramon jose","rjsa","rjsa")
    
    print(user.getNome())
    print(user.getUser())
    print(user.validate("rjsa","rjsa"))
    print(user.validate("rjsa","rjsb"))
if __name__ == "__main__":
    main()    