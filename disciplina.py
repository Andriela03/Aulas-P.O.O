class Disciplina:
    def __init__(self, nome, nota1, nota2, nota3, nota4):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def calcularmedia (self):
        media = (2*self.nota1 + 2*self.nota2 + 3*self.nota3 + 3*self.nota4)/10
        return media 
    
    def situacaofinal(self):
        m = self.calcularmedia()
        if m >= 60:
            return "Aprovado"
        elif m < 30:
            return "Reprovado" 
        else: 
            return"Prove final"

autoria_web = Disciplina("Autoria Web", 70, 80, 73, 90)
print(autoria_web.nome, autoria_web.calcularmedia())

print(autoria_web.nome, autoria_web.calcularmedia())



        