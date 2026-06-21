# Vou importar as classes daqui, para deixar o código organizado

from abc import ABC, abstractmethod

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