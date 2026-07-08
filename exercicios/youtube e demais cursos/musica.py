from classes import Musica

def main():
    class Song1(Musica):
        def exibir_detalhes(self):
            return f'O titulo atual é: {self.__titulo}\n O artista padrão é: {self.__artista}\n A duração em segundos: {self.__duracaoEmSegundos}'
        
    song1 = Song1()
    song1.exibir_detalhes()
    return

if __name__ == '__main__':
    main()