def exibir_agenda():
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
    minha_agenda[1]['nome'] = nome
    minha_agenda[1]['telefone'] = telefone
    minha_agenda[1]['email'] = email
    pass


minha_agenda = {1: {'nome': None, 'telefone': None,
                    'email': None, 'favorito': None}}


match exibir_agenda():
    case 1:
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone do contato: ')
        email = input('Digite o e-mail do contato: ')
        adicionar_contato(nome, telefone, email)

