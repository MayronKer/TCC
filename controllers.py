from views import app


@app.route('/simpan', methods=["POST"])
def simpan():
    nome = request.form['nome']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO computer (data) VALUES (%s);", (nome,))
    mysql.connection.commit()
    return redirect(url_for('home'))
