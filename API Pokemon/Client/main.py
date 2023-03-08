import requests

# print(pokemons)

# pokemon = {"id": 999, "nome": 'Zaurifus', "tipo": 'psycho', "hp": 100, "level": 99}
# url = 'http://127.0.0.1:5000/inserir-pokemons'
# requests.post(url, json=pokemon)

def verPokemons():
      pokemons = requests.get('http://127.0.0.1:5000/Pokemons').json()      
      for pokemon in pokemons:
            print(f'''
            Nome: {pokemon[1]}
            Tipo: {pokemon[2]}
            HP: {pokemon[3]}
            Level: {pokemon[4]}''')

def inserirPokemon():
      url = 'http://127.0.0.1:5000/inserir-pokemons'
      pokemon = {}
      pokemon['id'] = input("Digite o ID do Pokemon: ")
      pokemon['nome'] = input("Digite o nome do Pokemon: ")
      pokemon['tipo'] = input("Digite o tipo do Pokemon: ")
      pokemon['hp'] = input("Digite o HP do Pokemon: ")
      pokemon['level'] = input("Digite o level do Pokemon: ")
      requests.post(url, json=pokemon)
      
def deletarPokemon():
      url = 'http://127.0.0.1:5000/deletar-pokemons'
      pokemon = {}
      pokemon['id'] = input("Digite o ID do Pokemon que você quer deletar: ")
      requests.delete(url, json=pokemon)
      
def alterarPokemon():
    url = 'http://127.0.0.1:5000/atualizar-pokemons'
    pokemon = {}
    pokemon['id'] = input("Digite o ID do Pokemon que você quer alterar: ")
    pokemon['nome'] = input("Digite o nome do Pokemon: ")
    pokemon['tipo'] = input("Digite o tipo do Pokemon: ")
    pokemon['hp'] = input("Digite o HP do Pokemon: ")
    pokemon['level'] = input("Digite o level do Pokemon: ")
    requests.put(url, json=pokemon)

while True:
      print('''
            Digite a opcao desejada:
            1- Ver Pokemons
            2- Inserir Pokemon
            3- Alterar Pokemon
            4- Deletar Pokemon
            0- Sair
            ''')

      opcao = input("Digite a opção desejada: ")

      match opcao:
            case '1':
                  verPokemons()
            case '2':
                  inserirPokemon()
            case '3':
                  alterarPokemon()
            case '4':
                  deletarPokemon()
            case '0':
                  break
            case _:
                  print("Opção inválida")
