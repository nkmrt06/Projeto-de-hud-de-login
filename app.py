import customtkinter as ctk

#Configuração aparência
ctk.set_appearance_mode('dark')

#Criação das funções de funcionalidades
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    #Verificar se o usuario é Mariana e a senha 1612
    if usuario =='Mariana' and senha == '1612':
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')
    else:
        resultado_login.configure(text='Login incorreto',text_color='red')


#Criação da janela principal
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

#Criação dos campos

#Label
label_usuario = ctk.CTkLabel(app,text='Usuário:')
label_usuario.pack(pady=10)

#Entry
campo_usuario = ctk.CTkEntry(app,placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)

#Label
label_senha = ctk.CTkLabel(app,text='Senha:')
label_senha.pack(pady=10)

#Entry
campo_senha = ctk.CTkEntry(app,placeholder_text='Digite sua senha')
campo_senha.pack(pady=10)

#Button
botao_login = ctk.CTkButton(app,text='Login',command=validar_login)
botao_login.pack(pady=10)

#feedback de login

resultado_login = ctk.CTkLabel(app,text=' ')
resultado_login.pack(pady=10)


#Iniciar a aplicação

app.mainloop()