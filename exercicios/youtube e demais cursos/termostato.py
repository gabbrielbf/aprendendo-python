from classes import Termostato
from rich import inspect

def main():
    t = Termostato()
    t.ftemperatura
    t.temperatura = 20
    t.ftemperatura
    
    # inspect(t, private=True, methods=True)
    return

if __name__ == '__main__':
    main()