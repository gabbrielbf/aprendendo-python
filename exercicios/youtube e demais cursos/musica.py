from classes import Song1
from rich import inspect

def main():
    print()    
    song1 = Song1()
    print(song1.exibir_detalhes())
    print()
    song1.artista_setter = 'João Paulo'
    song1.titulo_setter = 'Galinha pintadinha'
    song1.duracao_setter = 120
    print(song1.exibir_detalhes())
    print()
    # song1.duracao_setter = -20 # <- Valor passado negativo propositalmente para captar erros de valor
    return

if __name__ == '__main__':
    main()