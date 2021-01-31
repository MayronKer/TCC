from views import app
from flask import redirect, url_for, request
from models import mysql

@app.route('/acao_login', methods=["POST", "GET"])
def acao_login():
    conexao = mysql.connection.cursor()
    conexao.execute("SELECT * FROM computer;")
    bd = conexao.fetchall()
    cur.close()
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
