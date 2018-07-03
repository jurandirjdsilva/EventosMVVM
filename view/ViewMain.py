from view import View
from hashlib import md5
from getpass import getpass

class ViewMain(View.View):
    def show(self):
        self.update()
        print(self.state)
        pass
        
def main():
    user = input("Usuario:")
    password = md5(getpass().encode()).hexdigest()
    print(user)
    print(password)
    pass 
    
if __name__ == "__main__":
    main()   