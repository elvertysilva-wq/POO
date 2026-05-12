class PlayList:

    def __init__(self, id, nome, descricao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)

    
    def set_id(self, id):
        if id < 0:
            raise ValueError('id não pode ser negativo')
        self.__id = id

    def set_nome(self, nome):
        if nome == "":
            raise ValueError('nome não pode ser vazio')
        self.__nome = nome

    def set_descricao(self, descricao):
        if descricao == "":
            raise ValueError('descrição não pode ser vazia')
        self.__descricao = descricao

   
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao

    # TOSTRING
    def __str__(self):
        return f"ID: {self.__id}, NOME: {self.__nome}, DESCRIÇÃO: {self.__descricao}"


class Musica:

    def __init__(self, id, titulo, artista, album):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)

    # SETS
    def set_id(self, id):
        if id < 0:
            raise ValueError('id não pode ser negativo')
        self.__id = id

    def set_titulo(self, titulo):
        if titulo == "":
            raise ValueError('titulo não pode ser vazio')
        self.__titulo = titulo

    def set_artista(self, artista):
        if artista == "":
            raise ValueError('música tem que haver artista')
        self.__artista = artista

    def set_album(self, album):
        if album == "":
            raise ValueError('música tem que haver álbum')
        self.__album = album

  
    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_artista(self):
        return self.__artista

    def get_album(self):
        return self.__album


    def __str__(self):
        return f"ID: {self.__id}, TITULO: {self.__titulo}, ARTISTA: {self.__artista}, ALBUM: {self.__album}"


class PlayListItem:

    def __init__(self, id, idPlayList, idMusica, sequencia):
        self.set_id(id)
        self.set_idPlayList(idPlayList)
        self.set_idMusica(idMusica)
        self.set_sequencia(sequencia)

  
    def set_id(self, id):
        if id < 0:
            raise ValueError('id não pode ser negativo')
        self.__id = id

    def set_idPlayList(self, idPlayList):
        if idPlayList < 0:
            raise ValueError('idPlaylist não pode ser negativo')
        self.__idPlayList = idPlayList

    def set_idMusica(self, idMusica):
        if idMusica < 0:
            raise ValueError('idMusica não pode ser negativo')
        self.__idMusica = idMusica

    def set_sequencia(self, sequencia):
        if sequencia < 0:
            raise ValueError('sequencia não pode ser negativa')
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
        return f"ID: {self.__id}, IDPLAYLIST: {self.__idPlayList}, IDMUSICA: {self.__idMusica}, SEQUENCIA: {self.__sequencia}"


class UI:
    #listas
    playlists = []
    musicas = []
    itens = []

    #main (op, wheli, op = UI.menu())
    @staticmethod
    def main():
        op = -1
        while op != 0:
            op = UI.menu()
            if op == 1: UI.inserir_playlist()
            if op == 2: UI.listar_playlists()
            if op == 3: UI.atualizar_playlist()
            if op == 4: UI.excluir_playlist()
            if op == 5: UI.inserir_musica()
            if op == 6: UI.listar_musicas()
            if op == 7: UI.atualizar_musica()
            if op == 8: UI.excluir_musica()
            if op == 9: UI.listar_musica_playlist()
            if op == 10: UI.transferir()
            if op == 11: UI.inserir_item()
            if op == 12: UI.listar_itens()
        print('Programa Encerrado.')
    #menu(print..., return int(input(...)))
    @staticmethod
    def menu():
        print('1 - inserir playlist')
        print('2 - listar playlists')
        print('3 - atualizar playlist')
        print('4 - excluir playlist')
        print('5 - inserir musica')
        print('6 - listar musicas')
        print('7 - atualizar musica')
        print('8 - excluir musica')
        print('9 - listar musicas de uma playlist')
        print('10 - transferir musica')
        print('11 - Adicionar Item')
        print('12 - Listar Itens')
        print('0 - Sair')
        return int(input('Escolha: '))
    
    #AS AÇÕES
    @classmethod
    def inserir_playlist(cls):
        id = int(input('ID da PlayList: '))
        nome = input('Nome: ')
        desc = input('Descrição: ')

        x = PlayList(id, nome, desc) #coloco no Objeto 
        cls.playlists.append(x) #coloco na lista
        print('Adicionada!')

    @classmethod
    def listar_playlists(cls):
        if len(cls.playlists) == 0: #vê se a lista não tá vazia
            print('Não há playlists cadastradas.')
        else:
            for x in cls.playlists: #vare a lista da playlist
                print(x) #ir printando as playlists

    @classmethod
    def atualizar_playlist(cls):
        id = int(input('ID da PlayList: ')) #pergunta qual a playlist

        for x in cls.playlists: #vare a lista de playlists
            if x.get_id() == id: #acha a playlist
                novo_nome = input('Novo Nome: ') #perguntar 
                nova_desc = input('Nova Descrição: ')

                x.set_nome(novo_nome) #substituir 
                x.set_descricao(nova_desc)
                print('Atualizada!')

    @classmethod
    def excluir_playlist(cls):
        id = int(input('ID da Playlist: '))

        for x in cls.playlists[:]:
            if x.get_id() == id:
                cls.playlists.remove(x)

                #remover os itens da playlist
                for item in cls.itens[:]:
                    if item.get_idPlayList() == id:
                        cls.itens.remove(item)
                print('Removida!')

    @classmethod
    def inserir_musica(cls):
        id = int(input('ID da Música: '))
        titulo = input('Título: ')
        artista = input('Artista: ')
        album = input('Album: ')

        x = Musica(id, titulo, artista, album)
        cls.musicas.append(x)
        print('Adicionada!')

    @classmethod
    def listar_musicas(cls):
        if len(cls.musicas) == 0: 
            print('Não há músicas cadastradas.')
        else:
            for x in cls.musicas:
                print(x)

    @classmethod
    def atualizar_musica(cls):
        id = int(input('ID da Música: '))

        for x in cls.musicas:
            if x.get_id() == id:
                novo_titulo = input('Novo Título: ')
                novo_artista = input('Novo Artista: ')
                novo_album = input('Novo Álbum: ')

                x.set_titulo(novo_titulo)
                x.set_artista(novo_artista)
                x.set_album(novo_album)
                print('Atualizada!')

    @classmethod
    def excluir_musica(cls):
        id = int(input('ID da Música: '))

        for x in cls.musicas:
            if x.get_id() == id:
                cls.musicas.remove(x)

                #remover os itens da música
                for item in cls.itens:
                    if item.get_idMusica() == id:
                        cls.itens.remove(item)
                print('Removida!')

    @classmethod
    def listar_musica_playlist(cls):
        id = int(input('ID da Playlist: '))

        for item in cls.itens:

         if item.get_idPlayList() == id:

            for musica in cls.musicas:

                if musica.get_id() == item.get_idMusica():
                    print(musica)

    @classmethod
    def transferir(cls):
        idMusica = int(input('ID da Música: '))
        novo_idPlaylist = int(input('Novo ID da Playlist: '))

        for item in cls.itens:
            if item.get_idMusica() == idMusica:
                item.set_idPlayList(novo_idPlaylist)
                print('Transferida!')

    @classmethod
    def inserir_item(cls):
        id = int(input('ID do Item: '))
        idPlayList = int(input('ID da Playlist: '))
        idMusica = int(input('ID da Música: '))
        seque = int(input('Sequência: '))

        x = PlayListItem(id, idPlayList, idMusica, seque)
        cls.itens.append(x)

        print('Item adicionado!')

    @classmethod
    def listar_itens(cls):
        if len(cls.itens) == 0:
            print('Não há itens.')
        else:
            for x in cls.itens:
                print(x)

UI.main()