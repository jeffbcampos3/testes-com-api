from flask import Flask, jsonify, make_response, Markup, request
from Controle.classConexao import Conexao
from Modelo.classPokemon import Pokemon

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

con = Conexao("localhost", "postgres", "jeff221988", "pokemons")

@app.route('/')
def home():
    return "API está no ar"

@app.route('/Pokemons')
def verPokemons():
    pokemons = con.querySelect(f'''SELECT * FROM pokemons;''')   
    
    return jsonify(pokemons) 
    
    # nomePokemon = pokemon.nome
    # tipoPokemon = pokemon.tipo
    # hpPokemon = pokemon.hp
    # levelPokemon = pokemon.level
    
    # # html = f'''<h1>{nomePokemon}</h1>
    # #         <h3>Tipo: {tipoPokemon}</h3>
    # #         <h3>HP: {hpPokemon}</h3>
    # #         <h3>Level: {levelPokemon}</h3>'''   
    
    # # return Markup(html)

@app.route('/inserir-pokemons', methods=['POST'])
def inserirPokemons():
    dados = request.json
    con.queryExecute(f'''INSERT INTO pokemons VALUES (
            {dados['id']},
            '{dados['nome']}',
            '{dados['tipo']}',
            {dados['hp']},
            {dados['level']})''')
    return 'deu'
    
@app.route('/deletar-pokemons', methods=['DELETE'])
def deletarPokemons():
    dados = request.json
    print(dados['id'])
    con.queryExecute(f'''DELETE FROM pokemons WHERE id = '{dados['id']}';''')
    return 'deu'

@app.route('/atualizar-pokemons', methods=['PUT'])
def alterarPokemon():
    dados = request.json
    print(dados)
    con.queryExecute(f'''UPDATE pokemons SET nome = '{dados['nome']}', tipo = '{dados['tipo']}', hp = {dados['hp']}, level = {dados['level']} WHERE id = '{dados['id']}';''')
    return 'deu'    
    

if __name__ == "__main__":
    app.run(debug=True)