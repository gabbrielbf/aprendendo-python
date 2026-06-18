
# Edição personalizada de prints ('Acho meio irrelevante').
from rich import print

print('Olá, [green]Mundo[/]! Estou aprendendo [red]classes[/]. :+1:')

# Importando caixas com cabeçarios personalizados
from rich.panel import Panel

caixa = Panel('Exibindo isto com cabeçario e contorno.')

print(caixa)

# Importando e usando TABELAS.
from rich.table import Table

tabela_precos = Table(title='Tabela de preços')
tabela_precos.add_column('Produto', justify='left', style='white')
tabela_precos.add_column('Preco', justify='center', style='green')

tabela_precos.add_row('Banana', '2,30')
tabela_precos.add_row('Coxinha', '4,50')

print(tabela_precos)

""" A melhor função disparada, conseguimos compreender melhor o que 
está armazenado no objeto sem ter a necessidade de um print organizado. """
from rich import inspect

inspect (int)

""" Importante também, devido as exibições de ERROS no terminal serem mais 
intuitivas e didádicas para a compreensão do problema. """
from rich.traceback import install
install()

# Função básica para retornar a divisão de dois números

def divisao(x: int, y: int):
    dividir = x/y
    return dividir

print(divisao(x=int(input('Digite X: ')), y=int(input('Digite Y: '))))

