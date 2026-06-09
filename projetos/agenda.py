import os
import time

def exibir_agenda():
    """ Função de exibição do menu """

    print(' ----- Minha agenda ----- ')
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
    """ Função para adicionar um contato """

    minha_agenda.append({'nome': nome, 'telefone': telefone,
                          'email': email, 'favorito': False})
    print()
    print(f'Contato: {nome} | {telefone} adicionado com sucesso!')
    return


def adicionar_mais_alguem():
    """ Função para definir se o usuário quer
    continuar adicionando pessoas. """

    print()
    print('1 - Adicionar mais alguém')
    print('0 - Voltar ao MENU')
    print('-' * 20)
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


def editar_somente_nome(agenda, indice_contato, nome):
    """ Função designada apenas para edição de nome do usuário """

    indice_contato_correto = indice_contato - 1
    if indice_contato_correto >= 0 and indice_contato_correto < len(minha_agenda):
        agenda[indice_contato_correto]['nome'] = nome
        print(f'Contato {indice_contato} atualizado com sucesso!')
    else:
        print('[ERRO]! O Indice é inválido!')
        print()
    return
    

def editar_somente_telefone(agenda, indice_contato, telefone):
    """ Função designada apenas para edição de telefone do usuário """

    indice_contato_correto = indice_contato - 1
    if indice_contato_correto >= 0 and indice_contato_correto < len(minha_agenda):
        agenda[indice_contato_correto]['telefone'] = telefone
        print(f'Contato {indice_contato} atualizado com sucesso!')
    else:
        print('[ERRO]! O Indice é inválido!')
        print()
    return


def editar_somente_email(agenda, indice_contato, email):
    """ Função designada apenas para edição de e-mail do usuário """

    indice_contato_correto = indice_contato - 1
    if indice_contato_correto >= 0 and indice_contato_correto < len(minha_agenda):
        agenda[indice_contato_correto]['email'] = email
        print(f'Contato {indice_contato} atualizado com sucesso!')
    else:
        print('[ERRO]! O Indice é inválido!')
        print()
    return
    

def editar_contato(agenda, indice_contato, nome, telefone, email):
    """ Função designada para edição de todos os dados do usuário """

    indice_contato_correto = indice_contato - 1
    if indice_contato_correto >= 0 and indice_contato_correto < len(minha_agenda):
        agenda[indice_contato_correto]['nome'] = nome
        agenda[indice_contato_correto]['telefone'] = telefone
        agenda[indice_contato_correto]['email'] = email
        print(f'Contato {indice_contato} atualizado com sucesso!')
    else:
        print('[ERRO]! O Indice é inválido!')
        print()
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
                visualizar_contatos(minha_agenda)
                indice_contato = int(input('Qual contato deseja editar: '))
                print('-' * 20)
                print('Qual dado abaixo deseja atualizar: ')
                print('-' * 20)
                print('1 - Nome')
                print('2 - Telefone')
                print('3 - E-mail')
                print('4 - Todos os dados')
                print('-' * 20)

                while True:
                    qual_dado_atualizar = int(input('Digite aqui -> '))
                    match qual_dado_atualizar:
                        case 1:
                            novo_nome = input('Digite o nome desejado: ').title()
                            editar_somente_nome(minha_agenda, indice_contato, novo_nome)
                            break
                        case 2:
                            novo_contato = input('Digite o CONTATO desejado: ')
                            editar_somente_telefone(minha_agenda, indice_contato, novo_contato)
                            break
                        case 3:
                            novo_email = input('Digite o E-MAIL desejado: ')
                            editar_somente_email(minha_agenda, indice_contato, novo_email)
                            break
                        case 4:
                            novo_nome = input('Digite o nome desejado: ').title()
                            novo_contato = input('Digite o CONTATO desejado: ')
                            novo_contato = input('Digite o E-MAIL desejado: ')
                            editar_contato(minha_agenda, indice_contato, novo_nome, novo_contato, novo_email)
                            break
                        case _:
                            print('Digite uma das opções acima!')
                            print()
                            continue
                
