import json
class Cliente:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)     
        self.set_id(nome)     
        self.set_id(email)     
        self.set_id(fone)
    def set_id(self, id):
        if id < 0: raise ValueError("") 
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("")   
