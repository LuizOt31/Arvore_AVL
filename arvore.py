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

    '''Calculo de Altura para os fatores de balanceamento'''
    def getHeight(self, raiz):
        if raiz is None:
            return -1
        return raiz.altura      

    def fatorBalanceamento(self, raiz):
        return self.getHeight(raiz.left) - self.getHeight(raiz.right)

    def atualizar_altura(self, raiz):
        raiz.altura = 1 + max(self.getHeight(raiz.right), self.getHeight(raiz.left))

    '''rotações simples'''
    #Rotação simples à direita
    def LL(self, raiz):
        X = raiz.left
        raiz.left = X.right
        X.right = raiz

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

        # raiz.left = self.RR(raiz.left)
        #         return self.LL(raiz)

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

    def busca(self, raiz, valor):
        if raiz is None:
            print("Elemento nao encontrado!")
            return None

        if raiz.chave == valor:
            print("Elemento encontrado!")
            return raiz
        elif valor < raiz.chave:
            return self.busca(raiz.left, valor)
        else:
            return self.busca(raiz.right, valor)

    # def remocao(self, raiz, valor):
    #     remove = self.busca(raiz, valor)
    #     if remove is None
        
    def delete_node(self, raiz, chave):
 
        # Find the node to be deleted and remove it
        if not raiz:
            return raiz
        elif chave < raiz.chave:
            raiz.left = self.delete_node(raiz.left, chave)
        elif chave > raiz.chave:
            raiz.right = self.delete_node(raiz.right, chave)
        else:
            if raiz.left is None:
                temp = raiz.right
                raiz = None
                return temp
            elif raiz.right is None:
                temp = raiz.left
                raiz = None
                return temp
            temp = self.avl_Minchave(raiz.right)
            raiz.chave = temp.key
            raiz.right = self.delete_node(raiz.right, temp.chave)
        if raiz is None:
            return raiz
 
        # Update the balance factor of nodes
        raiz.altura = 1 + max(self.getHeight(raiz.left), self.getHeight(raiz.right))
        fatorBalanceamento = self.fatorBalanceamento(raiz)
 
        # Balance the tree
        if fatorBalanceamento > 1:
            if self.avl_fatorBalanceamento(raiz.left) >= 0:
                return self.LL(raiz)
            else:
                # raiz.left = self.RR(raiz.left)
                # return self.LL(raiz)
                return self.LR(raiz)
        if fatorBalanceamento < -1:
            if self.fatorBalanceamento(raiz.right) <= 0:
                return self.RR(raiz)
            else:
                # raiz.right = self.LL(raiz.right)
                # return self.RR(raiz)
                return self.RL(raiz)
        return raiz

