from classes import Musica, Podcast, Playlist
from rich import inspect

def main():
    # Cria e configura os objetos da música
    musica1 = Musica()
    musica1.artista_setter = 'João Paulo'
    musica1.titulo_setter = 'Galinha pintadinha'
    musica1.duracao_setter = 120
    musica1.album_setter = 'Vaqueiro apaixonado'

    # Cria e configura os objetos do podcast
    podcast1 = Podcast()
    podcast1.titulo_setter = 'Live da madrugada'
    podcast1.host_setter = 'Podpah'
    podcast1.duracao_setter = 7500

    # Cria a playlist e adiciona os objetos criados acima
    playlist1 = Playlist()
    playlist1.playlist_setter = musica1
    playlist1.playlist_setter = podcast1

    # Execução
    playlist1.playlist_getter
    print()
    playlist1.duracao_playlist_getter
    print()
    playlist1.dar_play_em_tudo()

if __name__ == '__main__':
    main()