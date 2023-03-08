class Pokemon():
    def __init__(self, nome, tipo, hp, level):
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        self.level = level
        
    def infoPokemons(self):
        print(f'''              
              Nome: {self.nome}
              Tipo: {self.tipo}
              HP: {self.hp}
              Level: {self.level}
              ''')