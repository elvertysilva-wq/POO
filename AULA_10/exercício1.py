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
        if nome == "": raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    def set_estado(self, estado):
        if estado == "": raise ValueError("Estado não pode ser vazio")
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
    
class Jogador:
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
        if idTime < 0: raise ValueError("Id do time não pode ser vazio")
        self.__idTime = idTime
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
    times = []
    jogadores = []

    @staticmethod
    def main():
        op = -1
        while op != 0:
            op = UI.menu()
            if op == 1: UI.inserir_time()
            if op == 2: UI.listar_times()
            if op == 3: UI.atualizar_time()
            if op == 4: UI.excluir_time()
            if op == 5: UI.inserir_jogador()
            if op == 6: UI.listar_jogadores()
            if op == 7: UI.atualizar_jogador()
            if op == 8: UI.excluir_jogador()
            if op == 9: UI.listar_jogadores_time()
            if op == 10: UI.transferir()
        print('Programa Encerrado.')

    @staticmethod
    def menu():
        print('1 - inserir time')
        print('2 - listar times')
        print('3 - atualizar time')
        print('4 - excluir time')
        print('5 - inserir jogador')
        print('6 - listar jogadores')
        print('7 - atualizar jogador')
        print('8 - excluir jogador')
        print('9 - listar jogadores de um time')
        print('10 - transferir jogador')
        print('0 - Sair')
        return int(input('Escolha: '))

    #OPERAÇÕES
    #TIMES
    @classmethod
    def inserir_time(cls):
        id = int(input('ID: '))
        nome = input('Nome: ')
        estado = input('Estado: ')

        time = Time(id, nome, estado)
        cls.times.append(time)

        print('Time cadastrado!')

    @classmethod
    def listar_times(cls):
        if len(cls.times) == 0:
            print('Não há times cadastrados.')
        else:
            for x in cls.times:
                print(x)

    @classmethod
    def atualizar_time(cls):
        id = int(input('ID do time: '))

        for x in cls.times:
            if x.get_id() == id:
                print('Encontrado!')

                novo_nome = input('Novo Nome: ')
                novo_estado = input('Novo Estado: ')

                x.set_nome(novo_nome)
                x.set_estado(novo_estado)

                print('Atualizado!')

    @classmethod
    def excluir_time(cls):
        id = int(input('ID do Time: '))

        for x in cls.times:
            if x.get_id() == id:
                cls.times.remove(x)

                encontrou = True
                print('Removido!')

                for jogador in cls.jogadores:
                    if jogador.get_idTime() == id:
                        cls.jogadores.remove(jogador)

    #JOGADORES
    @classmethod
    def inserir_jogador(cls):
        id = int(input('ID do Jogador: '))
        idTime = int(input('ID do Time: '))
        nome = input('Nome: ')
        camisa = int(input('Camisa: '))

        jogador = Jogador(id, idTime, nome, camisa)
        cls.jogadores.append(jogador)
        print('Jogador cadastrado!')

    @classmethod
    def listar_jogadores(cls):
        if len(cls.jogadores) == 0:
            print('Não há jogadores cadastrados.')
        else:
            for x in cls.jogadores:
                print(x)

    @classmethod
    def atualizar_jogador(cls):
        id = int(input('ID do jogador: '))

        for x in cls.jogadores:
            if x.get_id() == id:
                novo_nome = input('Novo Nome: ')
                nova_camisa = int(input('Nova Camisa: '))

                x.set_nome(novo_nome)
                x.set_camisa(nova_camisa)
                print('Atualizado!')

    @classmethod
    def excluir_jogador(cls):
        id = int(input('ID do jogador: '))

        for x in cls.jogadores:
            if x.get_id() == id:
                cls.jogadores.remove(x)

                encontrou = True
                print('Excluído!')

    @classmethod
    def listar_jogadores_time(cls):
        id = int(input('ID do Time: '))

        for x in cls.jogadores:
            if x.get_idTime() == id:
                print(x)
    @classmethod
    def transferir(cls):
        id = int(input('ID do jogador: '))

        for x in cls.jogadores:
            if x.get_id() == id:
                print('Encontrei!')

                novo_idTime = int(input('Novo ID do Time: '))
                x.set_idTime(novo_idTime)
                print('Transferido!')
UI.main()