# Vou importar as classes daqui, para deixar o código organizado

from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print as rprint

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
        qtd_salarios = self.salario / self.salario_min
        return f"O salário de {self.nome} ({self.__class__.__name__}) é de\nR${self.salario:.2f} e corresponde a {qtd_salarios:.1f} salários mínimos."


class Pedreiro(Funcionario):
    def __init__(self, nome, val_hora, horas_trab):
        super().__init__(nome)
        self.val_hora = val_hora
        self.horas_trab = horas_trab
    
    def calc_salario(self):
        self.salario = (self.val_hora * self.horas_trab)
        return f'O valor do salário do pedreiro [{self.nome}] é: {self.salario:.2f}'
        

class Professor(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome)
        self.sal_bruto = sal_bruto
    
    def calc_salario(self):
        self.sal_liq = self.sal_bruto - (self.sal_bruto * (self.inss / 100))
        self.salario = self.sal_liq
        return f'O valor do salário do professor [{self.nome}] é: {self.salario:.2f}'
        

class Relatorio:
    @staticmethod
    def exibir(funcionario):
        funcionario.calc_salario()
        texto = funcionario.analisar_salario()
        rprint(Panel(texto, title="Análise de Salário", border_style="white"))

# Exercicio 1 - Sistema simples de pagamento
class MetodoPagamento(ABC):
    
    @abstractmethod
    def processar_pagamento(self, valor):
        pass


class CartaoCredito(MetodoPagamento):
    def processar_pagamento(self, valor):
        self.valor = valor
        return f'Processando valor de: R${self.valor:.2f} no crédito.'


class Pix(MetodoPagamento):
    def processar_pagamento(self, valor):
        self.valor = valor
        return f'Processando valor de: R${self.valor:.2f} no PIX.'
    
# Exercicio 2 - Sistema simples de notificações
class Notificador(ABC):
    
    @abstractmethod
    def enviar_mensagem(mensagem):
        pass


class Email(Notificador):
    def __init__(self, endereco_email):
        self.endereco_email = endereco_email
        return

    def enviar_mensagem(self, mensagem):
        return f'Enviando E-mail para: [{self.endereco_email}] -> {mensagem}'
  

class SMS(Notificador):
    def __init__(self, numero_telefone):
        self.numero_telefone = numero_telefone
        return
    
    def enviar_mensagem(self, mensagem):
        return f'Enviando SMS para: [{self.numero_telefone}] -> {mensagem}'
    

# Exercicio 3 - Sistema simples de relatórios
# Classes abstratas
class Relatorio(ABC):

    @abstractmethod
    def gerar_conteudo(dados):
        pass


class Exportador(ABC):

    @abstractmethod
    def exportar_conteúdo(conteudo):
        pass

# Classes concretas
class ExportarPDF(Exportador):
    def exportar_conteúdo(self, conteudo):
        PDF_exportado = f'Exportando para PDF: [{conteudo}]'
        return PDF_exportado


class ExportarTXT(Exportador):
    def exportar_conteúdo(self, conteudo):
        TXT_exportado = f'Exportando para TXT: [{conteudo}]'
        return TXT_exportado


# Classes Objetos
class RelatorioFinanceiro(Relatorio):
    
    def gerar_conteudo(self, dados):
        dados_financeiros = f'Tivemos R${dados:.2f} de lucro este mês!'
        return dados_financeiros


class RelatorioVendas(Relatorio):
    def gerar_conteudo(self, dados):
        dados_vendas = f'Tivemos {dados} vendas este mês!'
        return dados_vendas


# RPG Simples
import random
class Personagem(ABC):
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.vida = vida
        self.golpes = ['Ataque giratório', 'Voadora', 'Porrada com bastão']
        self.golpes = random.choice(self.golpes)
        return

    def atacar(self, alvo, forca):
        self.alvo = alvo
        self.forca = random.randint(0, forca)
        dano = self.forca
        self.receber_dano(dano)
        return

    def receber_dano(self, dano):
        dano = self.forca
        print(f'O jogador {self.nome} atacou o {type(self.alvo).__name__} com {self.golpes} e causou {dano} pontos de dano!')
        return 

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    
    def curar(self):
        print(f'O Guerreiro {self.nome} se curou com ataduras e recuperou {random.randint(0, 100)} pontos de vida!')
        return

class Mago(Personagem):

    def curar(self):
        print(f'O Mago {self.nome} se curou com uma poção e recuperou {random.randint(0, 100)} pontos de vida!')
        return


# Sistema de conta bancária para treinar encapsulamento
class ContaBancaria:

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.nome = nome
        self.saldo = saldo
        print(f'Conta N° {self.id} criada com sucesso\nSaldo atual é de: R${self.saldo:,.2f}')
    
    def __str__(self):
        return f'A conta {self.id} de {self.nome} tem {self.saldo:,.2f} de saldo.'
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:,.2f} autorizado na conta {self.id}')
        return

    def sacar(self, valor):
        self.saldo -= valor
        print(f'Saque de R${valor:,.2f} autorizado na conta {self.id}')
        return
        
