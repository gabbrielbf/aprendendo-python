def validar_senha(senha):
    if len(senha) >= 8:
        for letra in senha:
            if type(letra) in senha == int:
                return True
            else:
                continue
    return False

while True:

    senha = input('Digite a senha: ')

    if validar_senha(senha) == True:
        print('senha válida.')
        break
    else:
        print('senha inválida')
        continue

print('\nprograma finalizado\n')
    

