#Exemplo de herança
print("\nExemplo de herança:")
class Animal:
  def __init__(self, nome) -> None:
    self.nome = nome

  def andar(self):
    print(f"Oanimal {self.nome} andou")
    return

  def emitir_som(self):
    pass

class Cachorro(Animal):
  def emitir_som(self):
    return "Au, au"
  
class Gato(Animal):
  def emitir_som(self):
    return "Miau!"
  
dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")

print("\nExemplo de polimorfismo")
animais = [dog, cat]

for animal in animais:
  print(f"{animal.nome} faz: {animal.emitir_som()}")

class Pessoa:
    def __init__(self, nome='', idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
    
    def exibir_dados(self):
        print(f'Nome: {self.nome}| Idade: {self.idade}')


class Aluno(Pessoa):
    def __init__(self, nome='', idade=0, curso='', turma=''):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'O Aluno {self.nome} acabou de se matricular.')


class Professor(Pessoa):
    def __init__(self, nome='', idade=0, especialidade='', nivel=''):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'O Prof° {self.nome} começou a dar aula.')
        pass


class Funcionario(Pessoa):
    def __init__(self, nome='', idade=0, cargo='', setor='', salario=0):
      super().__init__(nome, idade)
      self.cargo = cargo
      self.setor = setor
      self.salario = salario

    def bater_ponto(self):
        print(f'A funcionária {self.nome} acabou de bater o ponto.')

    def exibir_dados(self):
        print(f'Nome: {self.nome} | Idade: {self.idade} | Salário: {self.salario}')

print()
a1 = Aluno('João', 17, 'Engenharia', '2° Ano')
a1.fazer_aniversario()
a1.fazer_matricula()

p1 = Professor('Marcos', 39, 'Engenharia de processos', 'Mestrado')
p1.fazer_aniversario()
p1.dar_aula()

f1 = Funcionario('Maria', 28, 'Limpeza', 'B2', 1500)
f1.fazer_aniversario()
f1.bater_ponto()
f1.exibir_dados()
print()

print("\nExemplo de encapsulamento:")
class ContaBancaria:
  def __init__(self, saldo) -> None:
    self.__saldo = saldo # Atributo privado

  def depositar(self, valor):
    if valor > 0:
      self.__saldo += valor

  def sacar(self, valor):
    if valor > 0 and valor <= self.__saldo:
      self.__saldo -= valor

  def consultar_saldo(self):
    return self.__saldo
    
conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=-500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor=2000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta_do_zezinho = ContaBancaria(saldo=50)

class Veiculo:
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo

  def ligar_veiculo(self):
    print(f'O veiculo {self.marca} - {self.modelo} ligou!')


class Moto(Veiculo):
  def __init__(self, marca, modelo):
    super().__init__(marca, modelo)

  def ligar_veiculo(self):
    print(f'A moto {self.marca} - {self.modelo} ligou usando os pedais.')
  
class Carro(Veiculo):
  def __init__(self, marca, modelo):
    super().__init__(marca, modelo)

  def ligar_veiculo(self):
    print(f'O carro {self.marca} - {self.modelo} ligou usando a chave.')


m1 = Moto('Yamaha', 'Factor')
c1 = Carro('Chevrolet', 'Celta')

m1.ligar_veiculo()
c1.ligar_veiculo()

# Cadastro simples de funcionários

class Funcionario:
    def __init__(self, nome='', salario=0):
        self.nome = nome
        self.salario = salario

    def bater_ponto(self):
        return f'O(a) Funcionário(a) {self.nome} bateu o ponto!'


class Gerente(Funcionario):
    def entrar_no_sistema(self):
        return f'O(a) Funcionário(a) {self.nome} entrou no sistema usando o login de ADM'
    

f1 = Funcionario('João', 1500.00)
g1 = Gerente('Maria', 3000.00)
print()

print(f1.bater_ponto())
print(g1.bater_ponto())
print(g1.entrar_no_sistema())
print(f1.entrar_no_sistema()) # <- O funcionário não consegue acessar a função de entrar no sistema pois é uma característica privada do gestor.