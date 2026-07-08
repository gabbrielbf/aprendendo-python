from classes import Midia1
from rich import inspect

def main():
    print()    
    # Testes com música
    midia1 = Midia1()
    print(midia1.exibir_detalhes())
    print()
    midia1.artista_setter = 'João Paulo'
    midia1.titulo_setter = 'Galinha pintadinha'
    midia1.duracao_setter = 120
    print(midia1.exibir_detalhes())
    print()
    # song1.duracao_setter = -20 # <- Valor passado negativo propositalmente para captar erros de valor

    # Testes com Album
    


    return

if __name__ == '__main__':
    main()