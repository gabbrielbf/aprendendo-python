# Implementando uma árvore binária

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None # <- Lembre-se que o modelo de árvore binária exige obrigatóriamente do dev a implementação de dois dados
        self.right = None # em seguimento de cascata

        return

    def __str__(self): # <- Serve para retornar uma string do dado fornecido 
        return str(self.data)
    
class BinaryTree: # <- Resoonável pela parte inteligente da árvore, manipulando os métodos e tratando os dados passados na classe Node()
    def __init__(self, data):
        node = Node(data) # Objeto criado para inserir um dado a ser trata-do como a raiz da árvore
        self.root = node

        return

def main():
    tree = BinaryTree(4) # <- Definindo a raiz da árvore
    tree.root.left = Node(11) # <- Valor da esquerda
    tree.root.right = Node(9) # <- Valor da direita

    print(tree.root)
    print(tree.root.left)
    print(tree.root.right)

if __name__ == '__main__':
    main()