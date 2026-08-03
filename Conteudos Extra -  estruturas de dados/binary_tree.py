# Implementando uma árvore binária

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None # <- Lembre-se que o modelo de árvore binária exige obrigatóriamente do dev a implementação de dois dados
        self.right = None # em seguimento de cascata

        return

    def __str__(self): # <- Serve para retornar uma string do dado fornecido 
        return str(self.data)
    
class BinaryTree: # <- Responsável pela parte inteligente da árvore, manipulando os métodos e tratando os dados passados na classe Node()
    def __init__(self, data=None):
        if data: # <- Modificação implementada para poder usar o BinaryTree sem precisar passar algum dado como parâmetro
            node = Node(data) # <- Objeto criado para inserir um dado a ser trata-do como a raiz da árvore
            self.root = node
        else:
            self.root = None

        return

    # método que faz o percurso em ordem simétrica
    def simetric_search(self, node=None):
        if node is None: # <- esse bloco confere se o nó está vazio, caso sim, percorra a partir da raiz
            node = self.root

        if node.left:
            print('(', end='') # <- exibindo parenteses de abertura antes de terminar a sub-árvore da esquerda
            self.simetric_search(node.left) # <- exibindo os itens sempre partindo da esquerda caso exista item na posição

        print(node, end='') # <- exibindo o item central com o "end='" para exibir tudo na mesma linha

        if node.right:
            self.simetric_search(node.right) # exibindo o próximo item, direita
            print(')', end='') # <- exibindo parenteses de abertura antes de terminar a sub-árvore da esquerda
        return

def main():
    # tree = BinaryTree(4) # <- Definindo a raiz da árvore
    # tree.root.left = Node(11) # <- Valor da esquerda
    # tree.root.right = Node(9) # <- Valor da direita

    # print(tree.root)
    # print(tree.root.left)
    # print(tree.root.right)

    tree = BinaryTree()
    n1 = Node('a')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('b')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('c')
    n8 = Node('d')
    n9 = Node('e')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    tree.root = n2
    tree.simetric_search()

    return

if __name__ == '__main__':
    main()