import sqlite3
from datetime import datetime, timedelta
#________________________________________________________________MODEL
#dao pode acabar chamando um atributo que ainda não foi definido, assim, o get poderá dar erro
class ComedouroRobo:
    def __init__(self, address): self.set_mac(address)
    def set_mac(self, mac): self.__mac = mac
    def set_rotacoes(self, rota): self.__rotacoes = rota
    def get_rotacoes(self): return self.__rotacoes
    def get_mac(self): return self.__mac
    def __str__(self): return f"robo_MAC ADDRESS: {self.__mac}"

class ReposicaoRacao:
    def __init__(self, iid, address, data): 
        self.set_mac(address)
        self.set_id(iid)
        self.set_data(data)
    def set_mac(self, mac): self.__mac = mac
    def set_id(self, idd): self.__id = idd
    def set_data(self, dt): self.__data = dt
    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_mac(self): return self.__mac
    def vencimento(self): return self.__data + timedelta(days= 35)
    def __str__(self): return f"ID: {self.__id} - DATA: {self.__data} - VENCIMENTO: {self.vencimento()} dias"

class Display:
    def __init__(self, address): self.set_mac(address)
    def set_mac(self, mac): self.__mac = mac
    def set_cor(self, cor): self.__cor = cor
    def set_tema(self, tema): self.__tema = tema
    def set_img(self, img): self.__img = img
    def get_mac(self): return self.__mac
    def get_cor(self): return self.__cor
    def get_tema(self): return self.__tema
    def get_img(self): return self.__img
    def __str__(self): return f"display_MAC ADDRESS: {self.__mac}"

#________________________________________________________________BANCO DE DADOS
class Database:
    conn = None
    nome_bd="agenda.db"
    
    @classmethod
    def abrir(cls):
        cls.conn = sqlite3.connect(cls.nome_bd)
        cls.conn.execute("PRAGMA foreign_keys = ON")
 
    @classmethod
    def fechar(cls):
        cls.conn.close()

    @classmethod
    def execute(cls, sql, params = None):
        cursor = cls.conn.cursor()
        cursor.execute(sql, params or [])
        cls.conn.commit()

    @classmethod
    def criar_tabelas(cls):
        cls.execute("""
            CREATE TABLE IF NOT EXISTS Comedouro_Robo (
                mac_address TEXT PRIMARY KEY NOT NULL,
                rotacoes INTEGER DEFAULT 3,
            );
        """)
        cls.execute("""
            CREATE TABLE IF NOT EXISTS Reposicao_Racao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mac_address TEXT UNIQUE NOT NULL,
                DT_reposicao TEXT NOT NULL,
                FOREIGN KEY (mac_address) REFERENCES Comedouro_Robo(mac_address)
            );
        """)
        cls.execute("""
            CREATE TABLE IF NOT EXISTS Display (
                mac_address TEXT PRIMARY KEY NOT NULL,
                cor TEXT DEFAULT '#7ed957',
                tema INTEGER DEFAULT 0,
                img TEXT,
                FOREIGN KEY (mac_address) REFERENCES Comedouro_Robo(mac_address)
            );
        """)

if __name__ == "__main__":
    Database.abrir()
    Database.criar_tabelas()
    Database.fechar()

#________________________________________________________________DAO

class ComedouroRoboDAO():
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO Comedouro_Robo (mac_address, rotacoes)
            VALUES (?, ?)
        """
        cls.execute(sql, (obj.get_mac(), obj.get_rotacoes())
        cls.fechar()

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE Comedouro_Robo SET rotacoes=?
            WHERE mac_address=?
        """
        cls.execute(sql, (obj.get_rotacoes(), obj.get_mac()))
        cls.fechar()

class ReposicaoDAO():
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO Reposicao_Racao (mac_address, DT_reposicao)
            VALUES (?, ?)
        """
        cls.execute(sql, (obj.get_mac(), obj.get_data())
        cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM Reposicao_Racao"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [ReposicaoRacao(id, mac, data) for (id, mac_address, DT_reposicao) in rows]
        cls.fechar()
        return objs

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM Reposicao_Racao WHERE id=?"
        cls.execute(sql, (obj.get_id(),))
        cls.fechar()

class DisplayDAO():
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO Display (mac_address, cor, tema, img)
            VALUES (?, ?, ?, ?)
        """
        cls.execute(sql, (obj.get_mac(), obj.get_data())
        cls.fechar()

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        #    if cor == "DEFAULT":
        sql = """
            UPDATE Display SET cor=?
            UPDATE Display SET tema=?
            UPDATE Display SET img=? 
            WHERE mac_address=?

        """
        cls.execute(sql, (obj.get_cor(), obj.get_tema(), obj.get_img(), obj.get_mac()))
        cls.fechar()
        



