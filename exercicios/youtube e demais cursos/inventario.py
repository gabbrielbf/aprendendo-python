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
    print(f'o produto {nome} foi adicionado com sucesso ✔️')
    return

def exibir_estoque():
    print('-'*30)
    for indice, produto in enumerate(estoque, start=1):
        print(f'produto {indice} - {produto['nome']:<8} | preço {produto['preco']:<4} | estoque {produto['qtd_inicial']}')
    print('-'*30)
    return

def vender_produto(venda:str, quantidade:int):
    
    valor_compra = 0.0

    for indice, item in enumerate(estoque):
        if venda == item['nome']:
            break
        raise Exception('produto não encontrado.')

    for indice, item in enumerate(estoque):
        if venda == item['nome']:
            if (item['qtd_inicial'] <= 0 or 
                quantidade > item['qtd_inicial']):
                raise Exception('estoque insuficiente.')
            else:
                valor_compra += (item['preco'] * quantidade)
                item['qtd_inicial'] -= quantidade
                if item['qtd_inicial'] < 0:
                    item['qtd_inicial'] = 0 # <- Essa linha de código foi criada puramente para exibir '0'
                                                        # quando o usuário selecionar a opção 2 no menu inicial
                print(f'você comprou {quantidade} unidades de {item['nome']} e o valor deu: {valor_compra}')
    return 

def repor_produto(produto:str, quantidade:int):

    for indice, item in enumerate(estoque):
        if produto == item['nome']:
            break
        raise Exception('produto não encontrado.')
    
    if quantidade <= 0:
        raise Exception('digite um valor maior que zero!')
    
    for indice, item in enumerate(estoque):
        if produto == item['nome']:
            item['qtd_inicial'] += quantidade
            print(f'estoque atualizado com sucesso ✔️\no produto {item['nome']} agora possui {item['qtd_inicial']} itens.')

def main():
    while True:
        limpar_interface()
        match exibir_menu():
            case 1:
                try:
                    nome_produto = str(input('digite o nome do produto: ')).title().strip()
                    preco_produto = float(input('digite o preço do produto: '))
                    qtd_produto = int(input('quantidade inicial do produto: '))
                except ValueError:
                    raise Exception('valor digitado inválido.')
                inserir_produto(nome_produto, preco_produto, qtd_produto)
            case 2:
                if not estoque:
                    raise Exception('estoque vazio!')
                exibir_estoque()
            case 3:
                exibir_estoque()
                try:
                    venda = str(input('o que deseja comprar -> ')).title().strip()
                    quantidade = int(input('quantas un. deseja comprar -> '))
                except ValueError:
                    raise Exception('valor digitado inválido.')
                vender_produto(venda, quantidade)
            case 4:
                exibir_estoque()
                try:
                    produto = str(input('qual produto deseja repor da lista acima -> ')).title().strip()
                    quantidade = int(input('quantas un. deseja repor -> '))
                except ValueError:
                    raise Exception('valor digitado inválido.')
                repor_produto(produto, quantidade)
            case 0:
                print('\nencerrando...\n')
                break
            case _:
                pass
        time.sleep(2)

if __name__ == '__main__':
    main()

