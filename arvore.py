# Trabalho Prático montar Arovore AVL balanceada
#
# rotação a esquerda, rotação a direita, rotação esquerda-direita,
# rotação direita-esquerda, inserção, remoção, pesquisa, percorrer estrutura, etc.
#
# LEMBRE-SE: x.b = Hleft - Hright sendo que x.b tem que estar entre {-1, 0, 1}
#

class AVLTree:
    def __init__(self, valor):
        self.key = valor
        self.altura = 0
        self.left = None
        self.right = None

    '''Calculo de Altura para os fatores de balanceamento'''


    '''rotações simples'''
    #Rotação simples à direita
    def LL(self, raiz):
        X = raiz.left
        raiz.left = X.right
        X.right = raiz

        self.atualizar_altura(raiz)
        self.atualizar_altura(X)
        return X  # retorna a nova raiz

    # Rotação simples à esquerda
    def RR(self, raiz):
        X = raiz.right
        raiz.right = X.left
        X.left = raiz

        self.atualizar_altura(raiz)
        self.atualizar_altura(X)
        return X  # retornando a nova raiz

    '''rotações duplas'''    
    #Rotação dupla à direita
    def LR(self, raiz):
        left_child = self.RR(raiz.left)
        raiz.left = left_child
        return self.LL(raiz)

    #Rotação dupla à esquerda
    def RL(self, raiz):
        right_child = self.LL(raiz.right)
        raiz.right = right_child
        return self.RR(raiz)

    '''Algoritmos de inserção, remoção e busca'''
    def insercao(self, chave):
        self.root = self._insercao()

    def _insercao(self, raiz, chave):
        if raiz is None:
            return AVLTree(chave)
        #continuar....        
