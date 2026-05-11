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
    
class Jogadores:
     #init
    def __init__(self, id, idTime ,nome, camisa):
        self.set_id(id) 
        self.set_idTime(idTime) 
        self.set_nome(nome) 
        self.set_camisa(camisa)
 #set
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_idTime(self, idTime):
        if idTime < 0: raise ValueError("Nome do time não pode ser vazio")
        self.__nome = idTime
    def set_nome(self, nome):
        if nome < 0: raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    def set_camisa(self, camisa):
        if camisa < 0: raise ValueError("Camisa não pode ser vazio")
        self.__camisa = camisa
    #get
    def get_id(self):
        return self.__id
    def get_idTime(self):
        return self.__idTime
    def get_nome(self):
        return self.__nome
    def get_camisa(self):
        return self.__camisa


    #ToString
    def __str__(self):
        return f"ID: {self.__id}, IDTIME: {self.__idTime}, NOME: {self.__nome}, CAMISA: {self.__camisa}"
    
class UI:
    #listas
    times = []
    jogadores = []
    #main
    op = -1
    while op != 0:
        op = UI.menu()
        if op == 1: UI.inserir_time()
        if op == 2: UI.listar_times()
        if op == 3: UI.atualizar_time()
    #menu
    def manu():
        print('1 - Inserir Time')
        print('1 - Inserir Time')
        print('1 - Inserir Time')
        print('1 - Inserir Time')
        print('1 - Inserir Time')
        print('1 - Inserir Time')
        print('1 - Inserir Time')
        print('1 - Inserir Time')
        print('1 - Inserir Time')
        print('1 - Inserir Time')
        return int(input('Escolha: '))
    #As operações

UI.main()



