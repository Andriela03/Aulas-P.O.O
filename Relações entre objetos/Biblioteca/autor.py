class Autor:
    def __init__(self, nome, nacionalidade, data_nascimento):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__data_nascimento = data_nascimento

    def get_nome(self):
        return self.__nome

    def get_nacionalidade(self):
        return self.__nacionalidade

    def get_dataNascimento(self):
        return self.__data_nascimento 

    def set_nome(self, nome):
        self.nome = nome 

    def set_nacionalidade(self, nacionalidade):
        self.nacionalidade = nacionalidade

    def set_dataNascimento(self, data_nascimento):
        self.dataNascimento = data_nascimento
