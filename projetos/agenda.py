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

    for contato in minha_agenda:

        """ O looping FOR está duplicando o conteúdo das variáveis dentro
        das chave: valor na minha_agenda, pensar em uma forma de conferir se a chave está
        vazia antes de preencher. """

        minha_agenda[contato]['nome'] = nome
        minha_agenda[contato]['telefone'] = telefone
        minha_agenda[contato]['email'] = email


def adicionar_mais_alguem():
    print()
    print('1 - Adicionar mais alguém')
    print('0 - Voltar ao MENU')
    print('----------')
    adicionar_outro = int(input('Deseja adicionar mais alguém? '))

    match adicionar_outro:
        case 1:
            return True
        case 0:
            return False


minha_agenda = {1: {'nome': None, 'telefone': None,
                    'email': None, 'favorito': None},
                2: {'nome': None, 'telefone': None,
                    'email': None, 'favorito': None},
                3: {'nome': None, 'telefone': None,
                    'email': None, 'favorito': None},
                4: {'nome': None, 'telefone': None,
                    'email': None, 'favorito': None}}


match exibir_agenda():
    case 1:
        while True:
            nome = input('Digite o nome do contato: ')
            telefone = input('Digite o telefone do contato: ')
            email = input('Digite o e-mail do contato: ')
            adicionar_contato(nome, telefone, email)
            print(minha_agenda)

            if adicionar_mais_alguem() == True:
                continue
            else:
                print('Voltando para o menu...')
                print()
                break
