#Tkinter
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

#Pillow
import PIL
from PIL import ImageTk, Image

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

frame_detalhes = Frame(janela, width=850, height=250, bg=cor4)
frame_detalhes.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=250, bg=cor3)
frame_tabela.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)


#Logo
app_lg = Image.open('./imagens/icon_aluno.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Gerenciador de Cursos", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=cor6, fg=cor1)
app_logo.place(x=0, y=0)

#Função Cadastro aluno
def cadastrar_aluno():
    print('cadastrar_aluno')
    
    
#Função Cadastro Curso
def cadastrar_curso():
    frame_tabela_curso = Frame(frame_tabela, frame_detalhes, width=850, height=620, bg=cor1)
    frame_tabela_curso.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

    l_nome_curso = Label(frame_tabela, text="Nome do curso *", height=1, anchor=NW, font='Ivy 12', bg=cor1, fg=cor4)
    l_nome_curso.place(x=4, y=10)
    e_nome_curso = Entry(frame_tabela, width=35, justify='left', relief='solid')
    e_nome_curso.place(x=7, y=40)
    
    l_duracao = Label(frame_tabela, text="Duração *", height=1, anchor=NW, font='Ivy 12', bg=cor1, fg=cor4)
    l_duracao.place(x=4, y=70)
    e_duracao = Entry(frame_tabela, width=20, justify='left', relief='solid')
    e_duracao.place(x=7, y=100)
    
    l_preco = Label(frame_tabela, text="Preço *", height=1, anchor=NW, font='Ivy 12', bg=cor1, fg=cor4)
    l_preco.place(x=4, y=130)
    e_preco = Entry(frame_tabela, width=10, justify='left', relief='solid')
    e_preco.place(x=7, y=160)
    
    l_professor = Label(frame_tabela, text="Professor", height=1, anchor=NW, font='Ivy 12', bg=cor1, fg=cor4)
    l_professor.place(x=4, y=190)
    e_professor = Entry(frame_tabela, width=35, justify='left', relief='solid')
    e_professor.place(x=7, y=220)
    
    
    botao_salvar = Button(frame_tabela, anchor=CENTER, text='Salvar' .upper(), width=10, overrelief=RIDGE, font=('Ivy 8 bold'), bg=cor3, fg=cor1)
    botao_salvar.place(x=7, y=290)
    
    
#Função ver aluno
def procurar_aluno():
    print('procurar_aluno')
    
    
#Função ver Curso
def procurar_curso():
    frame_tabela_curso = Frame(frame_tabela, frame_detalhes, width=850, height=620, bg=cor1)
    frame_tabela_curso.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)
    
    app_nome = Label(frame_tabela_curso, text="Tabela de Cursos", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
    app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

    list_header = ['ID','Curso','Duração','Preço', 'Professor']

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
    h=[170,150,80,160]
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
    #Cadastro de aluno
    if i == 'cadastrar_aluno':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
            
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        cadastrar_aluno()
        
    #Cadastro de Curso   
    if i == 'cadastrar_curso':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
            
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        cadastrar_curso()

    #Procurar aluno
    if i == 'procurar_aluno':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
            
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        procurar_aluno()
        
    #Cadastro de Curso   
    if i == 'procurar_curso':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
            
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