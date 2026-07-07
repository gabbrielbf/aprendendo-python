from classes import Pessoa, Aluno
from rich import inspect

def main():
    print('='*40)
    print('Criando e instânciando aluno')
    print('='*40)

    josue = Aluno('Josué', 2002)
    print(f'Josué nasceu no ano: {josue._nascimento}')
    print(f'Sua idade atual é:{josue.idade}')
    print(f'Os cursos disponíveis e atuais são: {josue.lista_cursos}')
    

    return

if __name__ == '__main__':
    main()