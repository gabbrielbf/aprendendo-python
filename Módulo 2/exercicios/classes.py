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
    def __init__(self, qtd_lados, lado):
        super().__init__(qtd_lados)
        self.lados = lado


class Cicrulo(Poligono):
    def __init__(self, qtd_lados, raio):
        super().__init__(qtd_lados)
        self.raio = raio