from views import app


@app.route('/acao_login', methods=["POST"])
def acao_login():
    return redirect(url_for('sobre'))
