from flask import Flask, request
from bcrypt import hashpw, gensalt
from psycopg2 import connect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


con = connect(
    host='containers-us-west-52.railway.app',
    user='postgres',
    password='AydSdSI4jWXIQZFY0atR',
    port=5461,
    database='railway'
)

@app.route('/')
def home():
    return 'API no AR'

@app.route('/cadastro', methods=['POST'])
def forms():
    usuario = request.json['usuario']
    email = request.json['email']
    senha = request.json['senha'].encode('utf-8')
    salt = gensalt()
    senha = hashpw(senha, salt).decode('utf-8')
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO usuario (usuario, email, senha) VALUES ('{usuario}', '{email}', '{senha}')")
    con.commit()
    con.close()
    print(usuario, email, senha)
    return 'foi'

if __name__ == '__main__':
    app.run(debug=True)