import uvicorn
from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get('/')
async def index():
    with sqlite3.connect('cadastro_alunos.db') as con:
        cur = con.cursor()
        query = 'SELECT * FROM cursos'
        cur.execute(query)
        data = cur.fetchall()
        
    return data
if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=8000)