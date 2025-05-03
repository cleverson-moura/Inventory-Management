from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DATABASE = 'estoque.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    return conn

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
    busca = request.args.get('pesquisa')
    with get_db_connection() as conn:
        if busca:
            cursor = conn.execute('SELECT * FROM produtos WHERE nome LIKE ?', ('%' + busca + '%',))
            produtos = cursor.fetchall()
        else:
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

        with get_db_connection() as conn:
            conn.execute('INSERT INTO produtos (nome,descricao,quantidade,preco) VALUES (?,?,?,?)',(nome,descricao,quantidade,preco))
        return redirect('/')
    return render_template('adicionar.html')

@app.route('/deletar/<int:id>')
def deletar(id):
    with get_db_connection() as conn:
        conn.execute('DELETE FROM produtos WHERE id = ?',(id,))
    return redirect('/')

@app.route('/atualizar/<int:id>', methods=['GET','POST'])
def atualizar(id):
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        quantidade = int(request.form['quantidade'])
        preco = float(request.form['preco'])

        with get_db_connection() as conn:
            conn.execute('UPDATE produtos SET nome = ?, descricao = ?, quantidade = ?, preco = ? where id = ?',(nome,descricao,quantidade,preco,id))
        return redirect('/')
    
    with get_db_connection() as conn:
        cursor = conn.execute('SELECT * FROM produtos WHERE id = ?',(id,))
        produto = cursor.fetchone()
    return render_template('atualizar.html', produto=produto)


if __name__ == '__main__':
    criar_tabela()
    app.run()