import requests

data = {'usuario': 'teste', 'email': 'teste@teste'}

# requests.post('http://localhost:5000/login', json=data)

dados = requests.get('http://localhost:5000/login').json()

print(dados)
