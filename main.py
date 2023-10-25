#Tkinter
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

#Pillow
import PIL
from PIL import ImageTk, Image

#Calendario
from tkcalendar import Calendar, DateEntry
from datetime import date

from view import *

# Cores
cor0 = "#000000"  # Preta
cor1 = "#feffff"  # Branca   
cor2 = "#e5e5e5"  # Cinza
cor3 = "#3CB371"  # Verde
cor4 = "#403d3d"   # letra
cor7 = "#ef5350"   # vermelha
cor6 = "#038cfc"   # Azul
cor8 = "#263238"   # + verde
cor9 = "#e9edf5"   # + verde

# Janela
janela = Tk()
janela.title("Gestão de Cursos")
janela.geometry('850x620')
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)
style = Style(janela)
style.theme_use("clam")

# Frames
frame_logo = Frame(janela, width=850, height=52, bg=cor6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_botoes = Frame(janela, width=850, height=65, bg=cor1)
frame_botoes.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_tabela = Frame(janela, width=850, height=620, bg=cor3)
frame_tabela.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)


#Logo
app_lg = Image.open('./imagens/icon_aluno.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Gerenciador de Cursos", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=cor6, fg=cor1)
app_logo.place(x=0, y=0)


#Logo instituição Janela "main"
#Logo
app_logo = Image.open('./imagens/sua_logo.png')
app_logo = app_logo.resize((300,300))
app_logo = ImageTk.PhotoImage(app_logo)
app_logo2 = Label(frame_tabela, image=app_logo, width=850, height=620, bg=cor1)
app_logo2.place(x=0, y=-50)


#Função Cadastro aluno
def cadastrar_aluno():
    frame_tabela_aluno = Frame(frame_tabela, width=850, height=620, bg=cor1)
    frame_tabela_aluno.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

    l_nome_aluno = Label(frame_tabela, text="Nome do aluno *", height=1, anchor=NW, font='Ivy 12', bg=cor1, fg=cor4)
    l_nome_aluno.place(x=4, y=10)
    e_nome_aluno = Entry(frame_tabela, width=35, justify='left', relief='solid')
    e_nome_aluno.place(x=7, y=40)
    
    l_data_nascimento = Label(frame_tabela, text="Data de Nascimento *", height=1, anchor=NW, font='Ivy 10', bg=cor1, fg=cor4)
    l_data_nascimento.place(x=4, y=70)
    data_nascimento = DateEntry(frame_tabela, width=18, background='darkblue', foreground='white', borderwidth=2, year=2023)
    data_nascimento.place(x=7, y=100)
    
    l_telefone = Label(frame_tabela, text="Telefone / Whatsapp *", height=1, anchor=NW, font='Ivy 12', bg=cor1, fg=cor4)
    l_telefone.place(x=4, y=130)
    e_telefone = Entry(frame_tabela, width=35, justify='left', relief='solid')
    e_telefone.place(x=7, y=160)
    
    l_endereco = Label(frame_tabela, text="Endereço *", height=1, anchor=NW, font='Ivy 12', bg=cor1, fg=cor4)
    l_endereco.place(x=4, y=190)
    e_endereco = Entry(frame_tabela, width=35, justify='left', relief='solid')
    e_endereco.place(x=7, y=220)
    
    l_email = Label(frame_tabela, text="Email *", height=1, anchor=NW, font='Ivy 12', bg=cor1, fg=cor4)
    l_email.place(x=500, y=130)
    e_email = Entry(frame_tabela, width=35, justify='left', relief='solid')
    e_email.place(x=500, y=160)
    
    c_sexo = ttk.Combobox(frame_tabela, width=20, font=('Ivy 8 bold'))
    c_sexo['values'] = ('Masculino', 'Feminino', 'Transgênero', 'Não-Binário', 'Não Informado')
    c_sexo.place(x=500, y=40)
    l_sexo = Label(frame_tabela, text="Gênero", height=1, anchor=NW, font='Ivy 12', bg=cor1, fg=cor4)
    l_sexo.place(x=500, y=7)
    
    l_cpf = Label(frame_tabela, text="CPF", height=1, anchor=NW, font='Ivy 12', bg=cor1, fg=cor4)
    l_cpf.place(x=500, y=70)
    e_cpf = Entry(frame_tabela, width=35, justify='left', relief='solid')
    e_cpf.place(x=500, y=100)
    
    l_foto = Label(frame_tabela, text="Foto", height=1, anchor=NW, font='Ivy 12', bg=cor1, fg=cor4)
    l_foto.place(x=500, y=190)
    global imagem, imagem_string, l_imagem
    def escolher_imagem():
        global imagem, imagem_string, l_imagem
        
        imagem = fd.askopenfilename()
        imagem_string = imagem
        
        imagem = Image.open(imagem)
        imagem = imagem.resize((130,130))
        imagem = ImageTk.PhotoImage(imagem)
        l_imagem = Label(frame_tabela, image=imagem, bg=cor1, fg=cor4)
        l_imagem.place(x=500, y=250)
        
        botao_carregar['text'] = 'Trocar foto'
        
    botao_carregar = Button(frame_tabela, command=escolher_imagem, text="Escolher Foto", width=15, compound=CENTER, overrelief=RIDGE, anchor=CENTER, font=('Ivy 10'), bg=cor1, fg=cor0)
    botao_carregar.place(x=500, y=220)
        
          
    botao_salvar = Button(frame_tabela, anchor=CENTER, text='Salvar' .upper(), width=10, overrelief=RIDGE, font=('Ivy 8 bold'), bg=cor3, fg=cor1)
    botao_salvar.place(x=7, y=300)
    
    
#Função Cadastro Curso
def cadastrar_curso():
    frame_tabela_curso = Frame(frame_tabela, width=850, height=620, bg=cor1)
    frame_tabela_curso.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)
    
    
    def novo_curso():
        nome = e_nome_curso.get()
        duracao = e_duracao.get()
        preco = e_preco.get()
        professor = e_professor.get()
        
        lista = [nome, duracao, preco, professor]
        
        for i in lista:
            if i == "":
                messagebox.showerror('Erro!', 'Preencha todos os campos')
                return
        
        criar_curso(lista)
        messagebox.showinfo('Sucesso!', 'Curso criado com sucesso!')
        
        e_nome_curso.delete(0, END)
        e_duracao.delete(0, END)
        e_preco.delete(0, END)
        e_professor.delete(0, END)
        

    l_nome_curso = Label(frame_tabela, text="Nome do curso *", height=1, anchor=NW, font='Ivy 12', bg=cor1, fg=cor4)
    l_nome_curso.place(x=4, y=10)
    e_nome_curso = Entry(frame_tabela, width=35, justify='left', relief='solid')
    e_nome_curso.place(x=7, y=40)
    
    l_duracao = Label(frame_tabela, text="Duração *", height=1, anchor=NW, font='Ivy 12', bg=cor1, fg=cor4)
    l_duracao.place(x=4, y=70)
    e_duracao = Entry(frame_tabela, width=35, justify='left', relief='solid')
    e_duracao.place(x=7, y=100)
    
    l_preco = Label(frame_tabela, text="Preço *", height=1, anchor=NW, font='Ivy 12', bg=cor1, fg=cor4)
    l_preco.place(x=4, y=130)
    e_preco = Entry(frame_tabela, width=35, justify='left', relief='solid')
    e_preco.place(x=7, y=160)
    
    l_professor = Label(frame_tabela, text="Professor", height=1, anchor=NW, font='Ivy 12', bg=cor1, fg=cor4)
    l_professor.place(x=4, y=190)
    e_professor = Entry(frame_tabela, width=35, justify='left', relief='solid')
    e_professor.place(x=7, y=220)
    
    
    botao_salvar = Button(frame_tabela, command=novo_curso, anchor=CENTER, text='Salvar' .upper(), width=10, overrelief=RIDGE, font=('Ivy 8 bold'), bg=cor3, fg=cor1)
    botao_salvar.place(x=7, y=290)

    
#Função ver aluno
def procurar_aluno():
    frame_tabela_aluno = Frame(frame_tabela, width=850, height=620, bg=cor1)
    frame_tabela_aluno.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)
    
    l_nome = Label(frame_tabela_aluno, text="Procurar Aluno: ", height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
    l_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)
    e_nome = Entry(frame_tabela_aluno, width=30, justify='left', relief='solid', font=('Ivy 10'))
    e_nome.place(x=125, y=8)
    
    botao_procurar = Button(frame_tabela, anchor=CENTER, text='Procurar', width=8, overrelief=RIDGE, font=('Ivy 8 bold'), bg=cor3, fg=cor1)
    botao_procurar.place(x=380, y=6)

    list_header = ['Nome','Data de Nascimento','Telefone','Curso']

    df_list = []

    global tree_aluno

    tree_aluno = ttk.Treeview(frame_tabela_aluno, selectmode="extended",columns=list_header, show="headings")

    vsb = ttk.Scrollbar(frame_tabela_aluno, orient="vertical", command=tree_aluno.yview)
    hsb = ttk.Scrollbar(frame_tabela_aluno, orient="horizontal", command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela_aluno.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","e","e"]
    h=[208,150,80,160]
    n=0

    for col in list_header:
        tree_aluno.heading(col, text=col.title(), anchor=NW)
        tree_aluno.column(col, width=h[n],anchor=hd[n])

    n+=1

    for item in df_list:
        tree_aluno.insert('', 'end', values=item) 

    
#Função ver Curso
def procurar_curso():
    frame_tabela_curso = Frame(frame_tabela, width=850, height=620, bg=cor1)
    frame_tabela_curso.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)
    
    l_curso = Label(frame_tabela_curso, text="Procurar Curso: ", height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
    l_curso.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)
    e_procurar_curso = Entry(frame_tabela_curso, width=30, justify='left', relief='solid', font=('Ivy 10'))
    e_procurar_curso.place(x=125, y=8)
    
    botao_procurar = Button(frame_tabela, anchor=CENTER, text='Procurar', width=8, overrelief=RIDGE, font=('Ivy 8 bold'), bg=cor3, fg=cor1)
    botao_procurar.place(x=380, y=6)

    list_header = ['Curso','Duração','Preço', 'Professor']

    df_list = []

    global tree_curso

    tree_curso = ttk.Treeview(frame_tabela_curso, selectmode="extended",columns=list_header, show="headings")

    vsb = ttk.Scrollbar(frame_tabela_curso, orient="vertical", command=tree_curso.yview)
    hsb = ttk.Scrollbar(frame_tabela_curso, orient="horizontal", command=tree_curso.xview)

    tree_curso.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_curso.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela_curso.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","e","e"]
    h=[208,150,80,160]
    n=0

    for col in list_header:
        tree_curso.heading(col, text=col.title(), anchor=NW)
        tree_curso.column(col, width=h[n],anchor=hd[n])

    n+=1

    for item in df_list:
        tree_curso.insert('', 'end', values=item)
#procurar_curso() ///////////////////////////////////


    
#Função Salvamento
def salvar():
    print('Salvar')
    
#Função Deletar
def deletar():
    print('Deletar')

#Função
def control(i):
    #Cadastro de Aluno
    if i == 'cadastrar_aluno':            
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        cadastrar_aluno()
        
    #Cadastro de Curso   
    if i == 'cadastrar_curso':
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        cadastrar_curso()

    #Procurar aluno
    if i == 'procurar_aluno':
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        procurar_aluno()
        
    #Procurar Curso   
    if i == 'procurar_curso':  
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        procurar_curso()

        

#Corpo
#Botões
#Novo Aluno
app_img_cadastro_aluno = Image.open('./imagens/icon_add_aluno.png')
app_img_cadastro_aluno = app_img_cadastro_aluno.resize((30,30))
app_img_cadastro_aluno = ImageTk.PhotoImage(app_img_cadastro_aluno)
app_cadastro = Button(frame_botoes, command=lambda:control('cadastrar_aluno'), image=app_img_cadastro_aluno, text="Criar Novo Aluno", width=425, compound=LEFT, relief=RAISED, anchor=N, font=('Ivy 15 bold'), bg=cor6, fg=cor1)
app_cadastro.place(x=0, y=0)

#Novo Curso
app_img_cadastro_curso = Image.open('./imagens/icon_add_curso.png')
app_img_cadastro_curso = app_img_cadastro_curso.resize((30,30))
app_img_cadastro_curso = ImageTk.PhotoImage(app_img_cadastro_curso)
app_cadastro = Button(frame_botoes, command=lambda:control('cadastrar_curso'), image=app_img_cadastro_curso, text="Criar Novo Curso", width=425, compound=LEFT, relief=RAISED, anchor=N, font=('Ivy 15 bold'), bg=cor6, fg=cor1)
app_cadastro.place(x=425, y=0)

#Procurar Aluno
app_img_procurar_aluno = Image.open('./imagens/icon_procurar_aluno.png')
app_img_procurar_aluno = app_img_procurar_aluno.resize((30,30))
app_img_procurar_aluno = ImageTk.PhotoImage(app_img_procurar_aluno)
app_procurar_aluno = Button(frame_botoes, command=lambda:control('procurar_aluno'), image=app_img_procurar_aluno, text="Procurar Aluno", width=425, compound=LEFT, relief=RAISED, anchor=N, font=('Ivy 15 bold'), bg=cor6, fg=cor1)
app_procurar_aluno.place(x=0, y=33)

#Procurar Curso
app_img_procurar_curso = Image.open('./imagens/icon_procurar_curso.png')
app_img_procurar_curso = app_img_procurar_curso.resize((30,30))
app_img_procurar_curso = ImageTk.PhotoImage(app_img_procurar_curso)
app_procurar_curso = Button(frame_botoes, command=lambda:control('procurar_curso'), image=app_img_procurar_curso, text="Procurar Curso", width=425, compound=LEFT, relief=RAISED, anchor=N, font=('Ivy 15 bold'), bg=cor6, fg=cor1)
app_procurar_curso.place(x=425, y=33)




# Executando a janela
janela.mainloop()