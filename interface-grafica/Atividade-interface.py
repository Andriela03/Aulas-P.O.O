from tkinter import *

janela = Tk()
frase1 = Label(janela, text="Hello World!", justify="left")
frase1.grid(row=0, column=0)
frase1["font"] = ("Inter", 15, "bold")
frase1["fg"] = "green"
frase1["bg"] = "white"

frase2 = Label(janela, text=" Tudo bem?", justify="right")
frase2.grid(row=1, column=0)
frase2["font"] = ("Inter", 15, "bold")
frase2["fg"] = "green"

frase3 = Label(janela, text="Lorem ipsum dolor sit amet. Ut unde aspernatur et omnis \n labore ut quasi velit. Eum minus voluptatem eos officiis \n mollitia  rem temporibus distinctio.", justify="left")
frase3.grid(row=2, column=0)
frase3["font"] = ("Inter", 12, "normal", "italic")
frase3["fg"] = "blue"

botao_sair = Button(janela)
botao_sair.grid(row=4, column=0)
botao_sair["text"] = "Sair"
botao_sair["width"] = 15
botao_sair["command"] = quit    


logo = PhotoImage(file="D:/Users/20231041110026/Desktop/Nova pasta-3/Aulas-P.O.O/interface-grafica/python.png")  
logo_label = Label(janela, image= logo)
logo_label.grid(row=3, column=0)
logo_label["width"] = 600
logo_label["height"] = 600
logo_label["bg"] = "black"


janela.mainloop()
