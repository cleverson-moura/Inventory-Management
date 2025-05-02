from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DATABASE = 'estoque.db'

def criar_tabela():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT,
                quantidade INTEGER NOT NULL,
                preco REAL NOT NULL
            );
        ''')

@app.route('/')
def index():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute('SELECT * FROM produtos')
        produtos = cursor.fetchall()
    return render_template('index.html', produtos=produtos)

@app.route('/adicionar', methods=['GET','POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        quantidade = int(request.form['quantidade'])
        preco = float(request.form['preco'])

        with sqlite3.connect(DATABASE) as conn:
            conn.execute('INSERT INTO produtos (nome,descricao,quantidade,preco) VALUES (?,?,?,?)',(nome,descricao,quantidade,preco))
        return redirect('/')
    return render_template('adicionar.html')

@app.route('/deletar/<int:id>')
def deletar(id):
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('DELETE FROM produtos WHERE id = ?',(id,))
    return redirect('/')

@app.route('/atualizar/<int:id>', methods=['GET','POST'])
def atualizar(id):
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        quantidade = int(request.form['quantidade'])
        preco = float(request.form['preco'])

        with sqlite3.connect(DATABASE) as conn:
            conn.execute('UPDATE produtos SET nome = ?, descricao = ?, quantidade = ?, preco = ? where id = ?',(nome,descricao,quantidade,preco,id))
        return redirect('/')
    
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute('SELECT * FROM produtos WHERE id = ?',(id,))
        produto = cursor.fetchone()
    return render_template('atualizar.html', produto=produto)


if __name__ == '__main__':
    criar_tabela()
    app.run()