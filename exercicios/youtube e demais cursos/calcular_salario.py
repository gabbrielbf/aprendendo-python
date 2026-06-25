from classes import *
from rich import inspect

def main():
    print()
    f1 = Pedreiro('Cleber', 12, 200)
    f1.calc_salario()
    f1.analisar_salario()
 
    f2 =  Professor('Jorge', 8000)
    f2.calc_salario()
    f2.analisar_salario()
    print()
    return

if __name__ == '__main__':
    main()