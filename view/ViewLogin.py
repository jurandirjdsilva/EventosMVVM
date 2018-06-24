from View import View
from getpass import getpass
from hashlib import md5 
class ViewLogin(View):
    pass

        
def main():
    user = input("Usuario:")
    password = md5(getpass().encode()).hexdigest()
    print(user)
    print(password)
    pass 
    
if __name__ == "__main__":
    main()   