class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som():
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f'{self.nome} está amamentando'
    
class Ave(Animal):
    pass