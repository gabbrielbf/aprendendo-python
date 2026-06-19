from rich import print, inspect
from classes import *

def main():
    polig = Cicrulo(12)

    print(f'Perimetro: {polig.perimetro():.1f}')
    print(f'Area: {polig.area():.1f}')

if __name__ == '__main__':
    main()