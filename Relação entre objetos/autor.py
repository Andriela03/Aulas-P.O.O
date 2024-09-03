class Autor:
    def __init__(self, nome, nacionalidade, dataNascimento):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__dataNascimento = dataNascimento

    def get_nome(self):
        return self.__nome

    def get_nacionalidade(self):
        return self.__nacionalidade

    def get_dataNascimento(self):
        return self.__dataNascimento 

    def set_nome(self, nome):
        self.nome = nome 

    def set_nacionalidade(self, nacionalidade):
        self.nacionalidade = nacionalidade

    def set_dataNascimento(self, dataNascimento):
        self.dataNascimento = dataNascimento
