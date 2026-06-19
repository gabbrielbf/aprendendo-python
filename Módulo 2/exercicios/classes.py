# Vou importar as classes daqui, para deixar o código organizado

from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, qtd_lados):
        super().__init__(qtd_lados)
        self.qtd_lados = qtd_lados

    def perimetro(self, qtd_lados):
        Lados = qtd_lados * 4
        return Lados
    
    def area(self, qtd_lados):
        Area = qtd_lados * qtd_lados
        return Area


class Cicrulo(Poligono):
    def __init__(self, qtd_lados, raio):
        super().__init__(qtd_lados)
        self.raio = raio

    def perimetro(self):
        Circulo = (2 * 3.14) * self.raio
        return Circulo
    
    def area(self):
        Area = 3.14 * self.raio**2
        return Area
