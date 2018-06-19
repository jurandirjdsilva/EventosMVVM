class Usuario ():
    def __init__(self,nome,usuario,senha):
        self.nome = nome
        self.usuario = usuario 
        self.senha = senha
    def setNome(self,nome):
        self.nome = nome
    def setUsuario(self,usuario):
        self.usuario = usuario
    def setSenha(self,senha):
        self.senha = senha
    def getNome(self):
        return self.nome
    def getUsuario(self):
        return self.usuario
    
    def autenticaUsuario(self,usuario,senha):
        if self.usuario==usuario and self.senha==senha:
            return True
        else : 
            return False
        
def main():
    usuario = Usuario("ramon jose","rjsa","rjsa")
    
    print(usuario.getNome())
    print(usuario.getUsuario())
    print(usuario.autenticaUsuario("rjsa","rjsa"))
    print(usuario.autenticaUsuario("rjsa","rjsb"))
if __name__ == "__main__":
    main()    