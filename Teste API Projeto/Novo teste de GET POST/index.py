from flask import Flask, request, jsonify 
from psycopg2 import connect

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

con = connect(
    host='containers-us-west-52.railway.app',
    user='postgres',
    port='5461',
    password='AydSdSI4jWXIQZFY0atR',
    database='railway'
)

dados_salvos = {}

@app.route('/')
def home():
    return 'AR'

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        cursor = con.cursor()
        usuario = request.json['usuario']
        email = request.json['email']
        cursor.execute(f'''SELECT * FROM usuario WHERE usuario = '{usuario}' AND email = '{email}';''')
        dadosUsuario = cursor.fetchone()
        print(dadosUsuario)
        dados = {}        
        dados['id'] = dadosUsuario[0]
        dados['usuario'] = dadosUsuario[1]
        dados['email'] = dadosUsuario[2]
        dados['senha'] = dadosUsuario[3]
        dados_salvos.update(dados)        
        return 'dados Salvos'
    elif request.method == 'GET':
        return jsonify(dados_salvos)

@app.route('/dados/', methods=['GET'])
def dados(dados):
    print(dados)
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)
        

        
    