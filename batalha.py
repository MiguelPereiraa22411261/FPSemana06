import json

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, inimigo):
        inimigo.vida -= self.ataque
        print(f"{self.nome} Ataca {inimigo.nome} e Causa {self.ataque} de Dano!")

    def __str__(self):
        return f"{self.nome} {self.vida}"

class Guerreiro(Personagem):
    def especial(self, inimigo):
        dano_especial = 30
        inimigo.vida -= dano_especial
        print(f"{self.nome} usa Golpe Poderoso em {inimigo.nome} e Causa {dano_especial} de Dano!")

class Mago(Personagem):
    def especial(self):
        cura = 25
        self.vida += cura
        print(f"{self.nome} usa Cura e Ganha {cura} Pontos de Vida!")

class Arqueiro(Personagem):
    def especial(self, inimigos):
        dano_especial = 15
        for inimigo in inimigos:
            if inimigo != self:
                inimigo.vida -= dano_especial
        print(f"{self.nome} usa Chuva de Flechas e Causa {dano_especial} de Dano a Todos os Inimigos!")
def importar_personagens(caminho):
    with open("personagens.json", "r") as file:
        dados = json.load(file)

    characters = []
    for dado in dados:
        classe = dado['classe']
        if classe == 'Guerreiro':
            characters.append(Guerreiro(dado['nome'], dado['vida'], dado['ataque']))
        elif classe == 'Mago':
            characters.append(Mago(dado['nome'], dado['vida'], dado['ataque']))
        elif classe == 'Arqueiro':
            characters.append(Arqueiro(dado['nome'], dado['vida'], dado['ataque']))

    return characters, len(characters)

def ordenar_personagens_por_vida(personagens):
    return sorted(personagens, key=lambda p: p.vida)

characters, num_characters = importar_personagens('personagens.json')
print(f"{num_characters} Personagens Entram em Batalha!")

characters = ordenar_personagens_por_vida(characters)

print(characters[0])
print(characters[1])
print(characters[2])

characters[0].atacar(characters[1])
print(characters[1])

characters[1].atacar(characters[2])
print(characters[2])

characters[2].atacar(characters[0])
print(characters[0])

characters[0].especial()
print(characters[0])

characters[1].especial([characters[0], characters[1]])
print(characters[0])
print(characters[1])

characters[2].especial(characters[1])
print(characters[1])