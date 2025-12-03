from datetime import datetime, timedelta

class ComedouroRobo:
    def __init__(self, address): self.set_mac(address)
    def set_mac(self, mac): self.__mac = mac
    def set_rotacoes(self, rota): self.__rotacoes = rota
    def set_rotinas(self, roti): self.__rotinas = roti
    def get_rotacoes(self): 
        try:    return self.__rotacoes
        except AttributeError: #Rotacoes pode ser opcional. Caso seja a iniciação do objeto no banco de dados, 
            #ele vai pro default, caso seja a atualização, fica o valor que já estava antes (possivelmente o default)
            pass
    def get_rotinas(self): 
        try:    return self.__rotinas
        except AttributeError: #Rotinas pode ser opcional. Caso seja a iniciação do objeto no banco de dados, 
            #ele vai pro default, caso seja a atualização, fica o valor que já estava antes (possivelmente o default)
            pass
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
    def get_mac(self): return self.__mac
    def get_cor(self): 
        try: return self.__cor
        except AttributeError: #Cor pode ser opcional. Caso seja a iniciação do objeto no banco de dados, 
            #ele vai pro default, caso seja a atualização, fica o valor que já estava antes (possivelmente o default)
            pass
    def get_tema(self): 
        return self.__tema
    def __str__(self): return f"display_MAC ADDRESS: {self.__mac}"