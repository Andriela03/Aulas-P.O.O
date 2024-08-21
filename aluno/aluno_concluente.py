from aluno_cursando import *
class Aluno_concluente(Aluno_cursando):
    def __init__(self, matricula, nome, curso, data_conclusao, emitiu_certificado):
        super().__init__(matricula, nome, curso, data_conclusao, emitiu_certificado)
        self.__data_conclusao = data_conclusao
        self.__emitiu_certificado = emitiu_certificado

    def get_data_conclusao(self):
        return(self.__data_conclusao)

    def get_emitiu_certificado(self):
        return(self.__emitiu_certificado)

    def set_data_conclusao(self, data_conclusao):
        self.__data_conclusao = data_conclusao

    def set_emitiu_certificado(self, emitiu_certificado):
        self.__emitiu_certificado = emitiu_certificado


concluinte = Aluno_concluente("20231041110026", "Andriela", "Informática", "2026", "2027")
concluinte.set_emitiu_certificado(True)
print(concluinte.get_matricula(), concluinte.get_nome(), concluinte.get_curso(), concluinte.get_data_conclusao(), concluinte.get_emitiu_certificado())


    
