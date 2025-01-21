from tkinter import *
import tkinter
from datetime import datetime

#Cores

cor1 = '#3d3d3d' #Preto
cor2 = '#fafcff' #Branco
cor3 = '#21c25c' #Verde
cor4 = '#E50914' #Vermelho
cor5 = '#dedcdc' #Cinza
cor6 = '#3080f0' #Azul


fundo = cor1
cor = cor2

janela = Tk()
janela.title('Relógio Digital')
janela.geometry('440x180')
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1)

def relogio():
    tempo= datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.strftime("%d")
    mes = tempo.strftime("%b") #B maiúsculo = "Janeiro", b minúsculo = "Jan" 
    ano = tempo.strftime("%Y") 
    l1.config(text=hora)

l1 = Label(janela, font=("Arial 80"), bg = fundo, fg = cor)
l1.grid(row = 0, column = 0, sticky = NW, padx = 5) 

l1 = Label(janela, text="21/01/25", font=("Arial 20"), bg = fundo, fg = cor4)
l1.grid(row = 0, column = 0, sticky = NW, padx = 5)

relogio()

janela.mainloop()
