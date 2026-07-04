from classes import Retangulo
from rich import inspect

def main():
    r = Retangulo()
    r.base = 12
    r.altura = 33
    r.medidas = (9, 3)

    inspect(r)
    
if __name__ == '__main__':
    main()