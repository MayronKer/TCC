# para conexão com BD e direcionamento entre as páginas
from flask_mysqldb import MySQL
from flask import redirect, url_for, request, Flask

# criando a aplicação
app = Flask(__name__)

# setups para o banco de dados
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'TCC'
mysql = MySQL(app)

# chamando rotas
import rotas


# funções para realizar o CRUD do usuário
@app.route('/acao_login', methods=["POST", "GET"])
def acao_login():
    # email = request.form['email']
    # senha = request.form['senha']
    # conexao = mysql.connection.cursor()
    # conexao.execute("SELECT id, email FROM usuario WHERE email = {} and senha = {};".format(email, senha))
    # bd = conexao.fetchall()
    # conexao.close()
    return redirect('sobre.html')

@app.route('/acao_cadastro', methods=["POST", "GET"])
def acao_cadastro():
    senha = request.form['senha']
    confirmarSenha = request.form['confirmarSenha']
    if senha == confirmarSenha :
        email = request.form['email']
        nome = request.form['nome'] + ' ' + request.form['sobrenome']
        dataCadastro = request.form['dataCadastro']
        genero = request.form['genero']
        dataNasc = request.form['dataNasc']
        conexao = mysql.connection.cursor()
        conexao.execute("INSERT INTO usuario (email, nome, senha, dataCadastro, genero, dataNasc) VALUES ('{}', '{}', '{}', '{}', {}, '{}');".format(email, nome, senha, dataCadastro, genero, dataNasc))
        mysql.connection.commit()
        return redirect('sobre.html')
    else :
        return redirect(url_for('cadastro', erroSenha = 'senhas não conferem'))
