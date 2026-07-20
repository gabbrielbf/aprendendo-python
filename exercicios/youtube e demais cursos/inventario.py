# Sistema de inventário de loja
def exibir_menu():
    print('-'*30)
    print('1 - adicionar produto')
    print('2 - visualizar estoque')
    print('3 - vender produto')
    print('4 - repor produto')
    print('0 - sair')
    print('-'*30)
    opcoes = (0, 1, 2, 3, 4)
    opcao = int(input('digite a opcao -> '))
    if opcao not in opcoes:
        raise Exception('opção digitada não encontrada!')
    else:
        return opcao
    
def inserir_produto(nome, preco, qtd_inicial):
    pass

