from tkinter import *

janela = Tk()
janela.title("Somador")
janela.geometry("300x300+100+100")

rotulo1 = Label(janela, text="Valor 1 :")
rotulo1.grid(row=0, column=0)

campo1 = Entry(janela)
campo1.grid(row=0, column=1)

rotulo2 = Label(janela, text="Valor 2:")
rotulo2.grid(row=1, column=1)

campo2 = Entry(janela)
campo2.grid(row=1, column=1)

rotulo3 = Label(janela, text="Resultado :")
rotulo3.grid(row=3, column=0)

campo3 = Entry(janela, state="disabled")
campo3.grid(row=9, column=1)



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
    subtracao = v1 - v1
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


botao = Button(janela)
botao.grid(row=2, column=1)
botao["width"] = 15 
botao["text"] = "Somar"
botao["command"] = somar

botao = Button(janela)
botao.grid(row=3, column=1)
botao["width"] = 15 
botao["text"] = "Subtrair"
botao["command"] = subtrair

botao = Button(janela)
botao.grid(row=3, column=1)
botao["width"] = 15 
botao["text"] = "Multiplicar"
botao["command"] = multiplicar

botao = Button(janela)
botao.grid(row=5, column=1)
botao["width"] = 15 
botao["text"] = "Dividir"
botao["command"] = dividir

janela.mainloop()