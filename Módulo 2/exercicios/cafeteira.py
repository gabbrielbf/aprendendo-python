from abc import ABC, abstractmethod

class BebidaQuente(ABC):

    def preparar(self):
        print('\n--- Iniciando Preparo ---')
        print(f'1. Fervendo água para beber ({self.nome_bebida})!')
        return
    
    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        print('--- Bebida pronta ---\n')
        pass

class Cafe(BebidaQuente):
    def __init__(self, nome_bebida=''):
        self.nome_bebida = nome_bebida
        return
    
    def preparar(self):
        super().preparar()
        self.misturar()
        self.servir()
        return 

    def misturar(self):
        print(f'2. Passando água quente dentre o café em pó.')
        return super().misturar()
    
    def servir(self):
        print(f'3. Servindo em xícara de vidro')
        return super().servir()
    
class Cha(BebidaQuente):
    def __init__(self, nome_bebida=''):
        self.nome_bebida = nome_bebida
        return
    
    def preparar(self):
        super().preparar()
        self.misturar()
        self.servir()
        return 

    def misturar(self):
        print(f'2. Derramando água encima de sachê.')
        return super().misturar()
    
    def servir(self):
        print(f'3. Servindo em xícara de porcelana')
        return super().servir()

class LeiteQuente(BebidaQuente):
    def __init__(self, nome_bebida=''):
        self.nome_bebida = nome_bebida
        return
    
    def preparar(self):
        super().preparar()
        self.misturar()
        self.servir()
        return 

    def misturar(self):
        print(f'2. Misturando com colher de pau.')
        return super().misturar()

    def servir(self):
        print(f'3. Servindo em copo térmico.')
        return super().servir()