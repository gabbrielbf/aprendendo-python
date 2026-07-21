import os, time

# Sistema de inventário de loja
estoque = []

def limpar_interface():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

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
    return opcao
    
def inserir_produto(nome:str, preco:float, qtd_inicial:int):
    estoque.append({'nome':nome, 'preco':preco, 'qtd_inicial':qtd_inicial})
    return

def exibir_estoque():
    print('-'*30)
    for indice, produto in enumerate(estoque, start=1):
        print(f'produto {indice} - {produto['nome']} | preço {produto['preco']} | estoque {produto['qtd_inicial']}')
    print('-'*30)
    return

def vender_produto(venda, quantidade):
    
    valor_compra = 0.0

    for indice in range(0, len(estoque)):
        if venda not in estoque[indice]['nome']:
            raise Exception('produto não encontrado.')

    for indice in range(0, len(estoque)):
        if venda == estoque[indice]['nome']:
            if estoque[indice]['qtd_inicial'] <= 0:
                raise Exception('estoque insuficiente.')
            else:
                valor_compra += estoque[indice]['preco']
                estoque[indice]['qtd_inicial'] -= quantidade
                if estoque[indice]['qtd_inicial'] < 0:
                    estoque[indice]['qtd_inicial'] = 0
                print(f'você comprou {estoque[indice]['nome']} e o valor deu: {valor_compra}')
    return valor_compra

def main():
    while True:
        limpar_interface()
        match exibir_menu():
            case 1:
                try:
                    nome_produto = str(input('digite o nome do produto: ')).title()
                    preco_produto = float(input('digite o preço do produto: '))
                    qtd_produto = int(input('quantidade inicial do produto: '))
                except ValueError:
                    raise Exception('valor digitado inválido.')
                inserir_produto(nome_produto, preco_produto, qtd_produto)
                print('produto adicionado com sucesso ✔️')
            case 2:
                if not estoque:
                    raise Exception('estoque vazio!')
                exibir_estoque()
            case 3:
                exibir_estoque()
                try:
                    venda = str(input('o que deseja comprar -> ')).title()
                    quantidade = int(input('quantas un. deseja comprar -> '))
                except ValueError:
                    raise Exception('valor digitado inválido.')
                
                vender_produto(venda, quantidade)
            case 4:
                pass
            case 0:
                print('\nencerrando...\n')
                break
            case _:
                pass
        time.sleep(1.5)

if __name__ == '__main__':
    main()

