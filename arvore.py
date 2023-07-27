'''
O código oferece uma árvore AVL com todas suas funcionalidades
Nosso grupo preferiu optar por fazer duas classes, a árvore em sí e os nós (os que guardam de fato o conteudo)

rotação a esquerda, rotação a direita, rotação esquerda-direita,
rotação direita-esquerda, inserção, remoção, pesquisa, percorrer estrutura, etc.

LEMBRE-SE: x.altura = Hleft - Hright sendo que x.b tem que estar entre {-1, 0, 1}

Ideias para melhorar no futuro: implementar em uma classe apenas!
'''
class No:
    def __init__(self, valor):
        self.valor = valor
        self.altura = 0
        self.left = None
        self.right = None

class ArvoreAVL(object):

    '''Calculo de Altura para os fatores de balanceamento e funções auxiliares'''

    #função auxiliar para a Remoção para achar menor valor na subarvore que precisa
    def MinimoValorDaArvore(self, root):
        if root is None or root.left is None:
            return root
        return self.MinimoValorDaArvore(root.left)

    def getAltura(self, raiz):
        if raiz is None:
            return -1
        return raiz.altura      

    def fatorBalanceamento(self, raiz):
        return self.getAltura(raiz.left) - self.getAltura(raiz.right)

    def atualizar_altura(self, raiz):
        raiz.altura = 1 + max(self.getAltura(raiz.right), self.getAltura(raiz.left))

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

    #função de inserir elemento na arvore com as rotações
    def insercao(self, raiz, valor):
        if raiz is None:
            return No(valor)
        
        if valor < raiz.valor:
            raiz.left = self.insercao(raiz.left, valor)
        else:
            raiz.right = self.insercao(raiz.right, valor)

        raiz.altura = 1 + max(self.getAltura(raiz.right), self.getAltura(raiz.left))
        balanceamento = self.fatorBalanceamento(raiz)

        if balanceamento > 1 and valor < raiz.left.valor:
            return self.LL(raiz)
        if balanceamento > 1 and valor > raiz.left.valor:
            return self.LR(raiz)
        if balanceamento < -1 and valor > raiz.right.valor:
            return self.RR(raiz)
        if balanceamento < -1 and valor <  raiz.right.valor:
            return self.RL(raiz)

        return raiz

    #funcao de busca por um valor, retorna o proprio nó
    def busca(self, raiz, valor):
        if raiz is None:
            print("Elemento nao encontrado!")
            return None

        if raiz.valor == valor:
            print("Elemento encontrado!")
            return raiz
        elif valor < raiz.valor:
            return self.busca(raiz.left, valor)
        else:
            return self.busca(raiz.right, valor)

    #função de remoção de um nó
    def remocao(self, raiz, valor):        
        if not raiz:
            return raiz
        elif valor < raiz.valor:
            raiz.left = self.remocao(raiz.left, valor)
        elif valor > raiz.valor:
            raiz.right = self.remocao(raiz.right, valor)
        else:
            if raiz.left is None:
                X = raiz.right
                raiz = None
                return X
            elif raiz.right is None:
                X = raiz.left
                raiz = None
                return X
            X = self.MinimoValorDaArvore(raiz.right)
            raiz.valor = X.valor
            raiz.right = self.remocao(raiz.right, X.valor)
        if raiz is None:
            return raiz
 
        raiz.altura = 1 + max(self.getAltura(raiz.left), self.getAltura(raiz.right))
        fatorBalanceamento = self.fatorBalanceamento(raiz)
 
        # Balancear
        if fatorBalanceamento > 1:
            if self.avl_fatorBalanceamento(raiz.left) >= 0:
                return self.LL(raiz)
            else:
                return self.LR(raiz)
        if fatorBalanceamento < -1:
            if self.fatorBalanceamento(raiz.right) <= 0:
                return self.RR(raiz)
            else:
                return self.RL(raiz)
        return raiz

    '''funcoes para percorrer a estrutura'''
    def preOrder(self, raiz):
        if not raiz:
            return
        print("{0} ".format(raiz.valor), end=" ")
        self.preOrder(raiz.left)
        self.preOrder(raiz.right)
    
    def inOrder(self, raiz):
        if not raiz:
            return
        self.inOrder(raiz.left)
        print("{0} ".format(raiz.valor), end=" ")
        self.inOrder(raiz.right)

    def postOrder(self, raiz):
        if not raiz:
            return
        self.postOrder(raiz.left)
        self.postOrder(raiz.right)
        print("{0} ".format(raiz.valor), end=" ")

    