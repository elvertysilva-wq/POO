class Time:
    #init
    def __init__(self, id, nome, estado):
        self.set_id(id) 
        self.set_nome(nome) 
        self.set_estado(estado) 
 #set
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome < 0: raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    def set_estado(self, estado):
        if estado < 0: raise ValueError("Estado não pode ser vazio")
        self.__estado = estado
    #get
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_estado(self):
        return self.__estado


    #ToString
    def __str__(self):
        return f"ID: {self.__id} NOME: {self.__nome}, ESTADO: {self.__estado}"
    
class TimeUI:
