from classes import Musica, Podcast, Playlist
from rich import inspect

def main():
    # Cria e configura os objetos da música
    musica1 = Musica()
    musica1.artista = 'João Paulo'
    musica1.titulo = 'Galinha pintadinha'
    musica1.duracao = 120
    musica1.album = 'Vaqueiro apaixonado'

    # Cria e configura os objetos do podcast
    podcast1 = Podcast()
    podcast1.titulo = 'Live da madrugada'
    podcast1.host = 'Podpah'
    podcast1.duracao = 7500

    # Cria a playlist e adiciona os objetos criados acima
    playlist1 = Playlist()
    playlist1.playlist = musica1
    playlist1.playlist = podcast1

    # Execução
    playlist1.playlist
    print()
    playlist1.duracao_playlist
    print()
    playlist1.dar_play_em_tudo()

if __name__ == '__main__':
    main()