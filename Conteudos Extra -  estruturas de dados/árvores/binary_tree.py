# Implementando uma árvore binária, esse arquivo será usado como base para todos os arquivos exemplo.py criados

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

    def posorder_search(self, node=None): # <- iniciando o valor do parâmetro para conseguir trabalhar sem inserir valores
        if node is None:
            node = self.root # <- se o nó estiver vazio, o nó passsa a ser a raiz

        if node.left:
            self.posorder_search(node.left) # conferindo primeiro a esquerda

        if node.right:
            self.posorder_search(node.right) # conferindo depois a direita
 
        print(node) # e por fim, exibindo a raiz, que no caso seria o nó da vez a ser exibido

    def height(self, node=None): # replicando o método acima aqui abaixo para calcular a altura de determinado lado de a árvore 
        if node is None:
            node = self.root 

        height_left = 0 # { valores iniciam com zero pois nas condicionais abaixo conferimos SE o valor do nó possui elemento
        height_right = 0 # } caso possua fazemos o cálculo, se não o valor se mantém em zero.

        if node.left:
            height_left = self.height(node.left) 

        if node.right:
            height_right = self.height(node.right) 

        # abaixo está a lógica do cálculo responsável pela altura do bloco
        if height_right > height_left:
            return height_right + 1
        else:
            return height_left + 1

class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None # <- variavel criada para conferência de tamanho do valor, por ex. testamos se x é maior y, caso seja jogamos x a direita
                        # caso não seja, irá ser alocado a esquerda.
        x = self.root
        while(x): # <- enquanto esse valor parâmetrado for diferente do vazio
            parent = x # <- vamos definir o parente pelo valor da vez na raiz 
            if value < x.data: # <- e em seguida vamos avançar esse valor do parente para alguma direção
                x = x.left
            else:
                x = x.right
        if parent is None: # <- isso aqui cria um nó com o valor parâmetrado para se tornar a raiz da árvore somente se CASO a raiz esteja vazia
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

# testando as primeira funcionalidade da árvore binária
def main():
    # tree = BinaryTree(4) # <- Definindo a raiz da árvore
    # tree.root.left = Node(11) # <- Valor da esquerda
    # tree.root.right = Node(9) # <- Valor da direita

    # print(tree.root)
    # print(tree.root.left)
    # print(tree.root.right)

    tree = BinaryTree()
    n1 = Node('7')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('8')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('25')
    n8 = Node('3')
    n9 = Node('9')

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
    expressão = (7+(8*((25/3)-9)))
    print(f' = {expressão:.2f}') # <- valores ilusórios para fins didáticos

    return

if __name__ == '__main__':
    main()