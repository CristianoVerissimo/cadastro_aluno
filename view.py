# Banco de dados SQLITE3 lite
import sqlite3 as lite

# Conexão com banco de dados
try:
    con = lite.connect('cadastro_alunos.db')
    print('Conexão com banco de dados realizada com sucesso!')
except lite.Error as e:
    print("Erro ao conectar com banco de dados", e)
    
# Tabela de Cursos
#Criar Cursos
def criar_cursos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Cursos (nome, duracao, preco) VALUES (?,?,?)"
        cur.execute(query,i)
        
#criar_cursos(['Violão','Semanas','10'])

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

print(listar_cursos())

#Atualizar Cursos
def atualizar_cursos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Cursos SET nome=?, duracao=?, preco=? WHERE id=?"
        cur.execute(query,i)

l = ['Violão', 'Tres Semanas', 10.0, 1]        
#atualizar_cursos(l)

#Deletar Cursos
def deletar_cursos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Cursos WHERE id=?"
        cur.execute(query,i)
        
#deletar_cursos([1])