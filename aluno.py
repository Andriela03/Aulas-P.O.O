class Aluno:
    def __init__(self, matricula, nome, curso):
        self.__matricula = matricula
        self.__nome = nome 
        self.__curso = curso

    def get_matricula(self):
        return(self.__matricula)
    
    def get_nome(self):
        return(self.__nome)

    def get_curso(self):
        return(self.__curso)

    def set_matricula(self, matricula):
        self.__matricula = matricula
        return(self.__matricula)

    def set_nome(self, nome):
        self.__nome = nome 
        return(self.__nome)

    def set_curso(self, curso):
        self.__curso = curso 
        return(self.__curso)

        



