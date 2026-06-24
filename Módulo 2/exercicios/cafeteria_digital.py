from cafeteira import *

lista_bebidas = ['Cafe', 'Cha', 'Leite']

def main():
    bebida = LeiteQuente()
    bebida.preparar(lista_bebidas[2])

if __name__ == '__main__':
    main()