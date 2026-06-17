class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som():
        pass


class Mamifero(Animal):
    def amamentar(self):
        return f'{self.nome} está amamentando'


class Ave(Animal):
    def voar(self):
        return f'{self.nome} está voando'


class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return 'Morcegos emitem sons ultrassônicos'
    

morcego = Morcego(nome='Batman')

# Acessando métodos da classe base 'Animal
print('Nome do morcego: ', morcego.nome)