#requisitos para sabermos:
#Click==7.0
#Flask==1.0.2
#Flask-MySQLdb==0.2.0
#get==2018.11.19
#itsdangerous==1.1.0
#Jinja2==2.10
#MarkupSafe==1.1.0
#mysqlclient==1.4.2
#post==2018.11.20
#public==2018.11.20
#query-string==2018.11.20
#request==2018.11.20
#Werkzeug==0.14.1

#OBS: lembrar de ligar xampp e acionar o database.

from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
mysql = MySQL(app)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM computer;")
    rv = cur.fetchall()
    cur.close()
    return render_template('home.html', computers=rv)
#salvar
@app.route('/simpan', methods=["POST"])
def simpan():
    nome = request.form['nome']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO computer (data) VALUES (%s);", (nome,))
    mysql.connection.commit()
    return redirect(url_for('home'))

#atualizar
@app.route('/update', methods=["POST"])
def update():
    id_data = request.form['id']
    nome = request.form['nome']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE computer SET data=%s WHERE id=%s;", (nome, id_data,))
    mysql.connection.commit()
    return redirect(url_for('home'))

#excluir
@app.route('/hapus/<string:id_data>', methods=["GET"])
def hapus(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM computer WHERE id=%s;", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
