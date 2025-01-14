from tkinter import *

janela = Tk()
janela.title("Somador")
janela.geometry("250x250+100+100")

rotulo1 = Label(janela, text="Valor 1:")
rotulo1.grid(row=0, column=1, pady=5)

campo1 = Entry(janela, width=20)
campo1.grid(row=0, column=2, pady=5)

rotulo2 = Label(janela, text="Valor 2:")
rotulo2.grid(row=1, column=1, pady=5)

campo2 = Entry(janela, width=20)
campo2.grid(row=1, column=2, pady=5)

rotulo3 = Label(janela, text="Resultado:")
rotulo3.grid(row=6, column=1, pady=5)

campo3 = Entry(janela, state="disabled", width=20)
campo3.grid(row=6, column=2, pady=5)



def somar():
    v1 = int(campo1.get())
    v2 = int(campo2.get())
    soma = v1 + v2 
    campo3.config(state="normal")
    campo3.delete(0, END)
    campo3.insert(0, soma)
    campo3.config(state="disable")


def subtrair ():
    v1 = int(campo1.get())
    v2 = int(campo2.get())
    subtracao = v1 - v2
    campo3.config(state="normal")
    campo3.delete(0, END)
    campo3.insert(0, subtracao)
    campo3.config(state="disable")


def multiplicar():
    v1 = int(campo1.get())
    v2 = int(campo2.get())
    multiplicacao = v1 * v2
    campo3.config(state="normal")
    campo3.delete(0, END)
    campo3.insert(0, multiplicacao)
    campo3.config(state="disable")


def dividir():
    v1 = int(campo1.get())
    v2 = int(campo2.get())
    divisao = v1 / v2
    campo3.config(state="normal")
    campo3.delete(0, END)
    campo3.insert(0, divisao)
    campo3.config(state="disable")


botao = Button(janela, width=20)
botao.grid(row=2, column=1, pady=5)
botao["width"] = 7
botao["bg"] = "yellow"
botao["text"] = "+"
botao["command"] = somar

botao = Button(janela, width=20)
botao.grid(row=3, column=1, pady=5)
botao["width"] = 7
botao["text"] = "-"
botao["bg"] = "lightgreen"
botao["command"] = subtrair

botao = Button(janela, width=20)
botao.grid(row=2, column=2, pady=5)
botao["width"] = 7 
botao["text"] = "x"
botao["bg"] = "pink"
botao["command"] = multiplicar

botao = Button(janela, width=20)
botao.grid(row=3, column=2, )
botao["width"] = 7
botao["text"] = "/"
botao["bg"] = "lightblue"
botao["command"] = dividir

janela.mainloop()