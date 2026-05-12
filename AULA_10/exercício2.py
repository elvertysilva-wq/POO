class PlayList:
    def __init__(self, id, nome, descrição):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descrição(descrição)

    def set_id(self, id):
        if id < 0: raise ValueError('id não pode ser negativo ')
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError('nome não pode ser vazio')
        self.__nome = nome
    def set_nome(self, descrição):
        if descrição == "": raise ValueError('descrição não pode ser vazia')
        self.__descrição = descrição
    
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_descrição(self):
        return self.__descrição
    
    def __str__(self):
        return f"ID: {self.__id}, NOME: {self.__nome}, DESCRIÇÃO: {self.__descrição}"


class Música:
    def __init__(self, id, artista, álbum):
        self.set_id(id)
        self.set_artista(artista)
        self.set_álbum(álbum)

    def set_id(self, id):
        if id < 0: raise ValueError('id não pode ser negativo ')
        self.__id = id
    def set_artista(self, artista):
        if artista == "": raise ValueError('música tem que haver artista')
        self.__artista = artista
    def set_álbum(self, álbum):
        if álbum == "": raise ValueError('música tem que haver álbum')
        self.__álbum = álbum
    
    def get_id(self):
        return self.__id
    def get_artista(self):
        return self.__artista
    def get_álbum(self):
        return self.__álbum
    
    def __str__(self):
        return f"ID: {self.__id}, ARTISTA: {self.__artista}, ÁLBUM: {self.__álbum}"

class PlayListItem:
    def __init__(self, id, idPlaylist, idMusica, sequencia):
        self.set_id(id)
        self.set_idPlayList(idPlaylist)
        self.set_idMusica(idMusica)
        self.set_sequencia(sequencia)

    def set_id(self, id):
        if id < 0: raise ValueError('id não pode ser negativo ')
        self.__id = id
    def set_idPlayList(self, idPlayList):
        if idPlayList < 0: raise ValueError('idPlaylist não pode ser negativo ')
        self.__idPlayList = idPlayList
    def set_idMusica(self, idMusica):
        if idMusica < 0: raise ValueError('idMusica não pode ser negativo ')
        self.__idMusica = idMusica
    def set_sequencia(self, sequencia):
        if sequencia < 0: raise ValueError('sequencia não pode ser negativa')
        self.__sequencia = sequencia
    
    def get_id(self):
        return self.__id
    def get_idPlayList(self):
        return self.__idPlayList
    def get_idMusica(self):
        return self.__idMusica
    def get_sequencia(self):
        return self.__sequencia

    
    def __str__(self):
        return f"ID: {self.__id}, IDPLAYLIST: {self.__PlayList}, IDMUSICA: {self.__idMusica}, SEQUENCIA: {self.__sequencia}"

class UI:
    playlist = []
    música = []
    itens_playlist = []

    @staticmethod
    def main():
        op = -1
        while op != 0:
            op = UI.menu()
            if op == 1: UI.inserir_playlist()
            if op == 2: UI.listar_playlist()
            if op == 3: UI.atualizar_playlist()
            if op == 4: UI.excluir_playlist()
            if op == 5: UI.inserir_música()
            if op == 6: UI.listar_música()
            if op == 7: UI.atualizar_música()
            if op == 8: UI.excluir_música()
            if op == 9: UI.inserir_itemplaylist()
            if op == 10: UI.listar_itemplaylist()
            if op == 11: UI.atualizar_itemplaylist()
            if op == 12: UI.excluir_itemplaylist()
            if op == 13: UI.transferir_itemplaylist()
        print('programa encerrado')
    
    @staticmethod
    def menu():
        print('1 - inserir playlist')
        print('2 - listar playlist')
        print('3 - atualizar playlist')
        print('4 - excluir playlist')
        print('5 - inserir música')
        print('6 - listar música')
        print('7 - atualizar música')
        print('8 - excluir música')
        print('9 - inserir item da playlist ')
        print('10 - listar item da playlist')
        print('11 - atualizar item da playlist')
        print('12 - excluir item da playlist')
        print('13 - transferir item da playlist')
        return int(input('Escolha: '))

    @classmethod
    def inserir_playlist(cls):
        id = int(input('ID: '))
        nome = (input('NOME: '))
        descrição = (input('DESCRIÇÃO: '))

        playlist = PlayList(id, nome, descrição)
        cls.playlists.append(playlist)

        print('PlayList cadastrada!')
    
@classmethod
def listar_playlist(cls):
    if len(cls.playlist) == 0:
        print('não há playlists cadastradas')
    else:
        for x in cls.playlists:
            print(x)
@classmethod
def atualizar_playlist(cls):
     id = int(input('ID do time: '))

     for x in cls.playlists:
            if x.get_id() == id:
                print('Encontrado!')

                novo_nome = input('Novo Nome: ')
                nova_descrição = input('Nova descrição: ')

                x.set_nome(novo_nome)
                x.set_descrição(nova_descrição)

                print('Atualizado!')
    
@classmethod
def excluir_playlist(cls):
    id = int(input('ID da PlayList: '))

    for x in cls.playlists:
        if x.get_id() == id:
            cls.playlists.remove(x)

            encontrou = True
            print('Removido!')

            for  in cls.jogadores:
                if jogador.get_idTime() == id:
                    cls.jogadores.remove(jogador)


   

    

UI.main()
    







            



        
        
        
        
