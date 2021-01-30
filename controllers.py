from views import app
from flask import redirect, url_for


@app.route('/acao_login', methods=["POST", "GET"])
def acao_login():
    return redirect('sobre.html')

@app.route('/acao_cadastro', methods=["POST", "GET"])
def acao_cadastro():
    return redirect('sobre.html')
