from classes import Musica, Podcast, Playlist
from rich import inspect

def musica():
    # Testes com música
    musica1 = Musica()
    print(musica1.exibir_detalhes())
    print()
    musica1.artista_setter = 'João Paulo'
    musica1.titulo_setter = 'Galinha pintadinha'
    musica1.duracao_setter = 120
    musica1.album_setter = 'Vaqueiro apaixonado'
    print(musica1.exibir_detalhes())
    print(musica1.dar_play())
    print()
    # song1.duracao_setter = -20 # <- Valor passado negativo propositalmente para captar erros de valor
    return

def podcast():
    # Testes com podcast
    podcast1 = Podcast()
    print(podcast1.exibir_detalhes())
    print()
    podcast1.titulo_setter = 'Live da madrugada'
    podcast1.host_setter = 'Podpah'
    podcast1.duracao_setter = 7500
    print(podcast1.exibir_detalhes())
    print(podcast1.dar_play())
    print()
    return

def main():
    musica()
    podcast()
    return

if __name__ == '__main__':
    main()