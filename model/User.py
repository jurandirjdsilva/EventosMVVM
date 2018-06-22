class User ():
    def __init__(self,name,email,user,password):
        self.email = email 
        self.name = name
        self.user = user 
        self.password = password   # armazenar em para md5
    def setName(self,name):
        self.name = name
    def setEmail(self,email):
        self.emal = emal
    def setUser(self,user):
        self.user = user
    def setSenha(self,password):
        self.password = password
    def getNome(self):
        return self.name
    def getUser(self):
        return self.user
    
    def validate(self,user,password):
        if self.user==user and self.password==password:
            return True
        else : 
            return False
        
def main():
    user = User("ramon jose","ramon.jsa@gmail.com","rjsa","rjsa")
    
    print(user.getNome())
    print(user.getUser())
    print(user.validate("rjsa","rjsa"))
    print(user.validate("rjsa","rjsb"))
if __name__ == "__main__":
    main()    