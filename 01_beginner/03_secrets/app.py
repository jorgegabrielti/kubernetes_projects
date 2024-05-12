from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configurar a conexão com o banco de dados
app.config['MYSQL_HOST'] = 'mysql-service'
app.config['MYSQL_USER'] = '' # Será injetado pelo Secret
app.config['MYSQL_PASSWORD'] = '' # Será injetado pelo Secret
app.config['MYSQL_DB'] = 'mydb'

# Estabelecer conexão com o banco de dados
mysql = mysql.connector.connect()

@app.route('/')
def index():
    cursor = mysql.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')