from tkinter import *

janela = Tk()

janela.title("Tela de login")
janela.geometry("220x100+100+100")

label_usuario = Label(janela, text="Usuário:")
label_usuario.grid(row=0, column=0)

entry_usuario = Entry(janela)
entry_usuario.grid(row=0, column=1)

label_senha = Label(janela, text="Senha:")
label_senha.grid(row=1, column=0)

entry_senha = Entry(janela, show="*")
entry_senha.grid(row=1, column=1)


def login():
    usuario = entry_usuario.get()  
    senha = entry_senha.get() 
    
    if usuario == "admin" and senha == "123456":
        label_resultado.config(text="Acesso permitido", fg="green")  
    else:  
        label_resultado.config(text="Acesso negado", fg="red")


botao_entrar = Button(janela, text="Entrar")
botao_entrar["command"] = login
botao_entrar.grid(row=2, column=0)

label_resultado = Label(janela, text="")  
label_resultado.grid(row=3, column=0)


janela.mainloop() 