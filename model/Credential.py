class Credential():
    def __init__(self,id,user,password):
        self.id = id
        self.user = user
        self.password = password   # armazenar em para md5
    
    def setUser(self,user):
        self.user = user
    def setPassword(self,password):
        self.password = password
    def getUser(self):
        return self.user
    
    def validate(self,user,password):
        if self.user==user and self.password==password:
            return True
        else : 
            return False

credentialList = []

def main():
    credential = Credential("1","rjsa","rjsa")
    print(credential.getUser())
    print(credential.validate("rjsa","rjsa"))
    print(credential.validate("rjsa","rjsb"))
if __name__ == "__main__":
    main()