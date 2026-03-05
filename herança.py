class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} esta comendo")


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)


class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)


class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)


Faisca = Gato("vira-lata", "preto e branco")

Faisca.comer()

Gardenia = Cachorro("lulu-pomerania", "branco")

Gardenia.comer()
