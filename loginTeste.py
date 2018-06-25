from view import ViewLogin
from viewmodel import ViewModelLogin
def main():
        visao =  ViewLogin.ViewLogin()
        visaoModelo = ViewModelLogin.ViewModelLogin()
        visaoModelo.attach(visao)
        visao.attach(visaoModelo)



if __name__ == "__main__":
    main()