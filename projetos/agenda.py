def exibir_agenda():
    """ Função de exibição do menu """

    print(' --- Minha agenda --- ')
    print('O que deseja fazer: ')
    print()
    print('1 - Salvar contato')
    print('2 - Editar contato')
    print('3 - Deletar contato')
    print('4 - Marcar um contato como favorito')
    print('0 - Sair')
    print()
    opcao = int(input('Digite uma das opções acima: '))
    return opcao


def adicionar_contato(nome, telefone, email):
    """ Função para adicionar um usuário """

    minha_agenda.append({'nome': nome, 'telefone': telefone,
                          'email': email, 'favorito': False})

    print(f'Contato: {nome} | {telefone} adicionado com sucesso!')
    return


def adicionar_mais_alguem():
    """ Função para definir se o usuário quer
    continuar adicionando pessoas. """

    print()
    print('1 - Adicionar mais alguém')
    print('0 - Voltar ao MENU')
    print('----------')
    while True:
        adicionar_outro = int(input('Deseja adicionar mais alguém? '))
        match adicionar_outro:
            case 1:
                adicionar_outro = True
                break
            case 0:
                adicionar_outro = False
                break
            case _:
                print('Opção inválida.')
                print()
                continue

    return adicionar_outro


def visualizar_contatos(agenda):
    print('Estes são seus contatos: ')
    for indice, contato in enumerate(minha_agenda, start=1):
        favorito = '❤️' if contato['favorito'] else ' '
        nome_contato = contato['nome']
        numero_contato = contato['telefone']
        email_contato = contato['email']
        print(f'{indice} - [{favorito}] | Nome: {nome_contato} | Número: {numero_contato} | E-mail: {email_contato}')
    print()
    return 


def editar_agenda(agenda, indice_contato):
    print('Qual contato deseja editar: ')
    visualizar_contatos(minha_agenda)

    
    
    return 


minha_agenda = []

while True:
    match exibir_agenda():
        case 0:
            print()
            print('Programa encerrado...')
            print()
            break
        case 1:
            while True:
                nome = input('Digite o nome do contato: ').title()
                telefone = input('Digite o telefone do contato: ')
                email = input('Digite o e-mail do contato: ')
                adicionar_contato(nome, telefone, email)

                if adicionar_mais_alguem() == True:
                    continue
                else:
                    print('Voltando para o menu...')
                    print()
                    break
        case 2:
            if minha_agenda == []:
                print('Você ainda não adicionou ninguém!')
                print()
                continue
            else:
                editar_agenda(minha_agenda)

