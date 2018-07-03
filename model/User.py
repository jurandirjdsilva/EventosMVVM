
class User:
    def __init__(self, name, email):
        self.email = email 
        self.name = name

    def set_name(self, name):
        self.name = name

    def se_email(self, email):
        self.email = email
    
    def get_nome(self):
        return self.name

    def get_email(self):
        return self.email

    def get_id(self):
        return self.id