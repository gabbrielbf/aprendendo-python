# Para esse projeto em específico, iremos trabalhar com uma outra estrutura de dados, porém linear, chamada Fila. Que se trata de remover o 
# primeiro item a entrar na mesma, e isso é justamente o que o percurso em nível faz! O primeiro item (no caso a raiz) é o primeiro a sair
# seguindo assim essa mesma metodologia para seus filhos.

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
 
        print(node) 

