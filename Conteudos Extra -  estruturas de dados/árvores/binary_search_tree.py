# Implementação de uma árvore binária de busca

import random
from binary_tree import BinarySearchTree

values = random.sample(range(1, 1001), 42) # <- função para retornar uma LISTA de 42 números inteiros únicos e sem repetição 
                                           # em um intervalo de 1 até 1000
binary_search_tree = BinarySearchTree()

for value in values:
    binary_search_tree.insert(value)

binary_search_tree.inorder_search()