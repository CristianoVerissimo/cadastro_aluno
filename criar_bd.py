# Banco de dados SQLITE3
import sqlite3

# Conexão com banco de dados
try:
    con = sqlite3.connect('cadastro_alunos.db')
    print('Conexão com banco de dados realizada com sucesso!')
except sqlite3.Error as e:
    print("Erro ao conectar com banco de dados", e)

# Tabela de Cursos
try:
    with con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS cursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            duracao TEXT,
            preco REAL,
            professor TEXT
        )""")
        
        print("Tabela de cursos criada com sucesso!")
        
except sqlite3.Error as e:
    print("Erro ao criar tabela de cursos", e)

# Tabela de Turmas
try:
    with con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            nome_cursos TEXT,
            data_inicio DATE,
            FOREIGN KEY (nome_cursos) REFERENCES cursos (nome) ON UPDATE CASCADE ON DELETE CASCADE
        )""")
        
        print("Tabela de turmas criada com sucesso!")
        
except sqlite3.Error as e:
    print("Erro ao criar tabela de turmas", e)

# Tabela de Alunos
try:
    with con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            data_nascimento DATE,
            telefone TEXT,
            endereco TEXT,
            email TEXT,
            sexo TEXT,
            foto TEXT,
            cpf TEXT,
            nome_turma TEXT,
            FOREIGN KEY (nome_turma) REFERENCES turmas (nome) ON DELETE CASCADE
        )""")
        
        print("Tabela de alunos criada com sucesso!")
        
except sqlite3.Error as e:
    print("Erro ao criar tabela de alunos", e)