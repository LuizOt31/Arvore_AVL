# Trabalho Prático montar Arovore AVL balanceada
#
# rotação a esquerda, rotação a direita, rotação esquerda-direita,
# rotação direita-esquerda, inserção, remoção, pesquisa, percorrer estrutura, etc.
#
# LEMBRE-SE: x.b = Hleft - Hright sendo que x.b tem que estar entre {-1, 0, 1}
#

class No:
    def __init__(self, valor):
        self.chave = valor
        self.altura = 0
        self.left = None
        self.right = None

class ArvoreAVL(object):
    '''rotações simples'''
    #Rotação simples à direita
    def LL(self, raiz):
        X = raiz.left
        T2 = X.right

        X.right = raiz
        raiz.left = T2

        self.atualizar_altura(raiz)
        self.atualizar_altura(X)

        return X  # retorna a NOva raiz

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

    def insercao(self, raiz, chave):
        if raiz is None:
            return No(chave)
        
        if chave < raiz.chave:
            raiz.left = self.insercao(raiz.left, chave)
        else:
            raiz.right = self.insercao(raiz.right, chave)

        raiz.altura = 1 + max(self.getHeight(raiz.right), self.getHeight(raiz.left))
        balanceamento = self.fatorBalanceamento(raiz)

        if balanceamento > 1 and chave < raiz.left.chave:
            return self.LL(raiz)
        if balanceamento > 1 and chave > raiz.left.chave:
            return self.LR(raiz)
        if balanceamento < -1 and chave > raiz.right.chave:
            return self.RR(raiz)
        if balanceamento < -1 and chave <  raiz.right.chave:
            return self.RL(raiz)

        return raiz

        

    '''Calculo de Altura para os fatores de balanceamento'''
    def getHeight(self, raiz):
        if raiz is None:
            return -1
        return raiz.altura
        #continuar....        

    def fatorBalanceamento(self, raiz):
        return self.getHeight(raiz.left) - self.getHeight(raiz.right)

    def atualizar_altura(self, raiz):
        raiz.altura = 1 + max(self.getHeight(raiz.right), self.getHeight(raiz.left))
