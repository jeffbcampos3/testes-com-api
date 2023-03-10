from dotenv import load_dotenv
from Controle.classConexao import Conexao
load_dotenv()
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from psycopg2 import Error

try:
    con = Conexao(host=os.getenv("HOST"), user=os.getenv("USER"), password=os.getenv("PASSWORD"), port=os.getenv("PORT"), database=os.getenv("DATABASE"))
        
    app = Flask(__name__)
    
    CORS(app)
    print("Conectado")
    
    @app.route("/filmes/<int:id>", methods =['GET' ,'POST'])
    def consultarFilmes(id):
      cursor = con.cursor()
      if(request.method == 'GET'):
        sql = f"SELECT * FROM filmes WHERE id_usuario = '{id}'"
        results = con.querySelect(sql)[0]        
        return results
      elif(request.method == 'POST'):
        titulo = request.json['titulo']
        id_usuario = request.json['id_usuario']
        sql = f"SELECT * FROM filmes WHERE titulo = '{titulo}' AND id_usuario = '{id_usuario}'"
        resposta = con.querySelect(sql)[0]        
        if(resposta is None):
          return jsonify({'status' : 'fail'})
        else:
          return jsonify({'status' : 'sucess'})
          
    @app.route("/series/<int:id>", methods =['GET'])
    def consultarSeries(id):
      sql = f"SELECT * FROM series WHERE id_usuario = '{id}'"
      results = con.querySelect(sql)[0]      
      return results
    
    @app.route("/listaDesejo/<int:id>", methods =['GET'])
    def consultarListaDesejo(id):
      sql = f"SELECT * FROM listaDesejo WHERE id_usuario = '{id}'"
      results = con.querySelect(sql)[0]      
      return results
    
    @app.route("/usuarios", methods =['POST'])
    def checarUsuarios():
      sql = f"SELECT * FROM usuarios WHERE email = '{email}' AND senha = '{senha}' "
      resposta = con.querySelect(sql)[0]      
      email = request.json['email']
      senha = request.json['senha']      
      if(resposta is None):
        return jsonify({'status' : 'fail'})
      else:
        return jsonify({'status' : 'sucess', 'id': f'{resposta[0]}', 'nome' : f'{resposta[1]}' })
          
    
    @app.route("/inserirFilme", methods =['POST'])
    def inserirFilme():
      sql = 'INSERT INTO filmes (titulo, imagem, nota, tipo, id_api, id_usuario) VALUES (%s, %s, %s, %s, %s, %s)', (titulo, imagem, nota, tipo, id_api, id_usuario)
      con.queryExecute(sql)        
      titulo = request.json['titulo']
      imagem = request.json['imagem']
      nota = request.json['nota']
      tipo = request.json['tipo']
      id_api = request.json['id_api']
      id_usuario = request.json['id_usuario']      
      return jsonify({'status': 'sucess'})
    
    @app.route("/inserirSerie", methods =['POST'])
    def inserirSerie():
      sql = 'INSERT INTO series (titulo, imagem, nota, tipo, id_api, id_usuario) VALUES (%s, %s, %s, %s, %s, %s)', (titulo, imagem, nota, tipo, id_api, id_usuario)
      con.queryExecute(sql)      
      titulo = request.json['titulo']
      imagem = request.json['imagem']
      nota = request.json['nota']
      tipo = request.json['tipo']
      id_api = request.json['id_api']
      id_usuario = request.json['id_usuario']      
      return jsonify({'status': 'sucess'})
    
    @app.route("/inserirListaDesejo", methods =['POST'])
    def inserirListaDesejo():
      sql = 'INSERT INTO listaDesejo (titulo, imagem, nota, tipo, id_api, id_usuario) VALUES (%s, %s, %s, %s, %s, %s)', (titulo, imagem, nota, tipo, id_api, id_usuario)
      con.queryExecute(sql)      
      titulo = request.json['titulo']
      imagem = request.json['imagem']
      nota = request.json['nota']
      tipo = request.json['tipo']
      id_api = request.json['id_api']
      id_usuario = request.json['id_usuario']     
      return jsonify({'status': 'sucess'})
    
    @app.route("/inserirUsuario", methods =['POST'])
    def inserirUsuario():
      sql = f"SELECT * FROM usuarios WHERE email = '{email}'"
      resposta = con.querySelect(sql)[0]     
      nome = request.json['nome']
      email = request.json['email']
      senha = request.json['senha']      
      if(resposta is None):
        sql = 'INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)', (nome, email, senha)
        con.queryExecute(sql)       
        return jsonify({'status': 'sucess'})
      else:  
        return jsonify({'status': 'fail'})
    
    @app.route("/removerListaDesejo", methods =['POST'])
    def removerListaDesejo():
      sql = f"SELECT * FROM listaDesejo WHERE titulo = '{titulo}' AND id_usuario = '{id_usuario}' "
      resposta = con.querySelect(sql)[0]     
      titulo = request.json['titulo']
      id_usuario = request.json['id_usuario']     
      if(resposta is None):
        return jsonify({'status' : 'fail'})
      else:
        sql = f"DELETE FROM listaDesejo WHERE titulo = '{titulo}'  AND id_usuario = '{id_usuario}'"
        con.queryExecute(sql)        
        return jsonify({'status': 'sucess'})
    
    @app.route("/removerFilme", methods = ['POST'])
    def removerFilme():
      sql = f"DELETE FROM filmes WHERE id_usuario = '{id_usuario}' AND titulo = '{titulo}'"
      con.queryExecute(sql)     
      titulo = request.json['titulo']
      id_usuario = request.json['id_usuario']     
      return jsonify({'status' : 'sucess'})
    if __name__ == '__main__':
      app.run(debug=True)
except(Error) as error:
  print(error)

