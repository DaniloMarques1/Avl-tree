class Musica:
    def __init__(self, nome=None, autor=None, album=None, ano=None):
        self._nome = nome
        self._autor = autor
        self._album = album
        self._ano = ano

    def set_nome(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome

    def set_autor(self, autor):
        self._autor = autor

    def get_autor(self):
        return self._autor

    def set_album(self, album):
        self._album = album

    def get_album(self):
        return self._album

    def set_ano(self, ano):
        self._ano = ano

    def get_ano(self):
        return self._ano
