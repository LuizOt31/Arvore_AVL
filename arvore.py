# Trabalho Prático montar Arovore AVL balanceada
#
# rotação a esquerda, rotação a direita, rotação esquerda-direita,
# rotação direita-esquerda, inserção, remoção, pesquisa, percorrer estrutura, etc.
#
# LEMBRE-SE: x.b = Hleft - Hright {-1, 0, 1}
#

class AVLTree:
    def __init__(self, valor):
        self.key = valor
        self.altura
        self.left_child = None
        self.right_child = None

'''rotação a direita'''
def LL(raiz):
    X = raiz.left
    y = X.right
    raiz.left = y
    X.right = raiz

    X.altura = FatorBalanco(X)
    return X #retorna a nova raiz

'''rotação a esquerda'''
def RR(raiz):
    X = raiz.right
    y = X.left
    raiz.right = y
    X.left = raiz

    X.altura = FatorBalanco(X)
    return X #retornando a nova raiz

'''rotação dupla'''    
def LR(raiz):
    RR(raiz.left)
    LL(raiz)

'''rotação dupla'''
def RL(raiz):
    LL(raiz.right)
    RR(raiz)

def FatorBalanco(raiz):
    return raiz.left.altura - raiz.right.altura

'''Algoritmos de inserção, remoção e busca'''


