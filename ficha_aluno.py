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
cor0 = "#2e2d2b"  # Preta
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

frame_detalhes = Frame(janela, width=850, height=200, bg=cor1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=cor1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)


#Logo
app_lg = Image.open('./imagens/icon_ver_aluno.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Ficha Aluno", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=cor6, fg=cor1)
app_logo.place(x=0, y=0)

# Executando a janela
janela.mainloop()