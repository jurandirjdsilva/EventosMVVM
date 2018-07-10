# conecta_db.py
import sqlite3

class Connect(object):
    def __init__(self,db_name):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()

        except sqlite3.Error:
            print("Erro ao abrir o banco")
            return False
    def close_db(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada")

def main():
    banco = Connect("EventosMVVM.db")
    banco.close_db()


if __name__ == "__main__":
    main()