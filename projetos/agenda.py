def exibir_agenda():
    """ Função de exibição do menu """
    
    print(' --- Minha agenda --- ')
    print('O que deseja fazer: ')
    print()
    print('1 - Salvar contato')
    print('2 - Editar contato')
    print('3- Deletar contato')
    print('4 - Marcar um contato como favorito')
    print('0 - Sair')
    print()
    opcao = int(input('Digite uma das opções acima: '))
    return opcao


def adicionar_contato(nome, telefone, email):
    """ Função para adicionar um usuário """

    if minha_agenda == '':
        minha_agenda = {}

    """ Parei aqui tentando solucionar a lógica da adição de adição 
    de um novo dicionário com os dados do usuário """

    for contato in range(1, len(minha_agenda)):

        minha_agenda[contato] = {'nome': None, 'telefone': None,
                    'email': None, 'favorito': None}

        minha_agenda[contato]['nome'] = nome
        minha_agenda[contato]['telefone'] = telefone
        minha_agenda[contato]['email'] = email


minha_agenda = {}

variavel_temporaria = {1: {'nome': None, 'telefone': None,
                    'email': None, 'favorito': None}}

match exibir_agenda():
    case 1:
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone do contato: ')
        email = input('Digite o e-mail do contato: ')
        adicionar_contato(nome, telefone, email)

