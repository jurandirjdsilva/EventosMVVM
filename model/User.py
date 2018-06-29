class User ():
    def __init__(self,id,name,email):
        self.id = id
        self.email = email 
        self.name = name
    def setId(self,id):
        self.id = id
    def setName(self,name):
        self.name = name
    def setEmail(self,email):
        self.email = email
    
    def getNome(self):
        return self.name
    def getEmail(self):
        return self.email
    def getId(self):
        return self.id
    
        
def main():
    
    user = User("42","ramon jose","ramon.jsa@gmail.com")
    
    print(user.getId())
    print(user.getNome())
    print(user.getEmail())
    
    user.setId("45")
    user.setName("ramon jose de sousa araujo")
    user.setName("ramon.jsa@hotmail.com")
    
    print(user.getId())
    print(user.getNome())
    print(user.getEmail())
    
if __name__ == "__main__":
    main()    