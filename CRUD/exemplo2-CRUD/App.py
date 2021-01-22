from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conex db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdb'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

# routes
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', productos = data)

@app.route('/add_producto', methods=['POST'])
def add_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        marca = request.form['marca']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO productos (nombre, precio, marca) VALUES (%s,%s,%s)", (nombre, precio, marca))
        mysql.connection.commit()
        flash('Adicionado!')
        return redirect(url_for('Index'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_producto(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-producto.html', producto = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_producto(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        marca = request.form['marca']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE productos
            SET nombre = %s,
                marca = %s,
                precio = %s
            WHERE id = %s
        """, (nombre, marca, precio, id))
        flash('Atualizado!')
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_producto(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM productos WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Excluído:(')
    return redirect(url_for('Index'))

# starting the app
if __name__ == "__main__":
    app.run(debug=True)

'''
if __name__ == "__main__":
    app.run(port=3000, debug=True)
'''
