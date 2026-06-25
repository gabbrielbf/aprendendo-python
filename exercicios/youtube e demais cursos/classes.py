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
    def __init__(self, distancia):
        self.distancia = distancia
        return 

    @abstractmethod
    def calc_frete(self):
        pass

""" Perceba que nas classes a baixo não definiremos o '__init__' PRESENTE na classe 'Transporte', não que isso seja uma regra até porquê
se colocarmos os inits nas classes filhas abaixo o código funcionará da mesma maneira. Porém a falta de presença desse '__init__' nos ensina
uma coisa importante na execução do programa. O código começa a rodar; Ele verá que a classe moto tem um argumento (x) dentro do objeto instânciado mas 
quando ele entra no bloco da classe percebe que ela não possui um '__init__', sendo assim vai na classe mãe buscar esse '__init__' e lá o
encontrará. Caso não tivessemos '__init__' na classe mãe ele nos daria um erro. """

class Moto(Transporte):
    def calc_frete(self):
        self.fator = 0.5
        self.frete = (self.distancia * self.fator)
        return f'{self.frete:.2f}'

  
class Caminhao(Transporte):
    def calc_frete(self):
        self.fator = 1.2
        if self.distancia >= 50:
            self.frete = (self.distancia * self.fator)
            return f'{self.frete:.2f}'
        else:
            return f'Caminhões fazem corridas acima de 50Km '


class Drone(Transporte):
    def calc_frete(self):
        self.fator = 9.5
        if (self.distancia > 0 and 
            self.distancia <= 10):
            self.frete = (self.distancia * self.fator)
            return f'{self.frete:.2f}'
        else:
            return f'O drone não tem bateria para viagens acima de [{self.distancia}Km], o limite é 10. '
        
# Calcular salário de diferentes funcionários

class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome 
        self.salario_min = 1612
        self.inss = 7.5
        return
    
    @abstractmethod
    def calc_salario(self):
        pass

    def analisar_salario(self):
        self.qtd_salarios = (self.salario / self.salario_min)
        print(f'O salário {self.salario:.2f} corresponde a {self.qtd_salarios:.1f} salários mínimos.')
        return


class Pedreiro(Funcionario):
    def __init__(self, nome, val_hora, horas_trab):
        super().__init__(nome)
        self.val_hora = val_hora
        self.horas_trab = horas_trab
    
    def calc_salario(self):
        self.salario = (self.val_hora * self.horas_trab)
        print(f'O valor do salário do pedreiro [{self.nome}] é: {self.salario:.2f}')
        return 


class Professor(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome)
        self.sal_bruto = sal_bruto
    
    def calc_salario(self):
        self.sal_liq = self.sal_bruto - (self.sal_bruto * (self.inss / 100))
        self.salario = self.sal_liq
        print(f'O valor do salário do professor [{self.nome}] é: {self.salario:.2f}')
        return

