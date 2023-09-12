# Banco de dados SQLITE3 lite
import sqlite3 as lite

# Conexão com banco de dados
try:
    con = lite.connect('cadastro_alunos.db')
    print('Conexão com banco de dados realizada com sucesso!')
except lite.Error as e:
    print("Erro ao conectar com banco de dados", e)
    
# ////////////////////Tabela de Cursos////////////////////

# Criar Curso
def criar_curso(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Cursos (nome, duracao, preco) VALUES (?, ?, ?)"
        cur.execute(query, i)

# Listar Cursos
def listar_cursos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Cursos')
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista

# Atualizar Curso
def atualizar_curso(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Cursos SET nome=?, duracao=?, preco=? WHERE id=?"
        cur.execute(query, i)

l = ['Violão', 'Tres Semanas', 10.0, 1]        
# atualizar_curso(l)

# Deletar Curso
def deletar_curso(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Cursos WHERE id=?"
        cur.execute(query, i)

# deletar_curso([1])

# ////////////////////Tabela de Turmas////////////////////

# Criar Turma
def criar_turma(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Turmas (nome, nome_cursos, data_inicio) VALUES (?, ?, ?)"
        cur.execute(query, i)

# Listar Turmas
def listar_turmas():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Turmas')
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista

# Atualizar Turma
def atualizar_turma(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Turmas SET nome=?, nome_cursos=?, data_inicio=? WHERE id=?"
        cur.execute(query, i)

# Deletar Turma
def deletar_turma(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Turmas WHERE id=?"
        cur.execute(query, i)

# ////////////////////Tabela de Alunos////////////////////

# Criar Aluno
def criar_aluno(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Alunos (nome, email, telefone, sexo, imagem, data_nascimento, cpf, nome_turma) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

# Listar Alunos
def listar_alunos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Alunos')
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista

# Atualizar Aluno
def atualizar_aluno(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Alunos SET nome=?, email=?, telefone=?, sexo=?, imagem=?, data_nascimento=?, cpf=?, nome_turma=? WHERE id=?"
        cur.execute(query, i)

# Deletar Aluno
def deletar_aluno(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Alunos WHERE id=?"
        cur.execute(query, i)