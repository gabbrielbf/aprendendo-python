# Vou importar as classes daqui, para deixar o código organizado

from abc import ABC, abstractmethod

# Classes dos poligonos
class Poligonos(ABC):
    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligonos):
    def __init__(self, lado):
        self.lado = lado 

    def perimetro(self):
        return self.lado * 4
    
    def area(self):
        return self.lado * self.lado


class Circulo(Poligonos):
    def __init__(self, raio):
        self.raio = raio
        self.pi = 3.14 

    def perimetro(self):
        return 2 * self.pi * self.raio
    
    def area(self):
        return self.pi * (self.raio * self.raio)

# Classes da cafeteria
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
    
# Classes dos calculos de frete
class Transporte(ABC):
    def distancia(self):
        return

    def frete(self):
        return

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    def __init__(self):
        
        return
    
    def calc_frete(self):
        
        return 