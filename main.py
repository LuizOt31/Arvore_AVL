from arvore import No
from arvore import ArvoreAVL

# Criacao uma árvore vazia
arvore = ArvoreAVL()

# Inserindo os elementos na árvore
raiz = None
elementos = [50, 25, 20, 30]
for elemento in elementos:
    raiz = arvore.insercao(raiz, elemento)

# Printando a raiz
print("Raiz:")
print(raiz.valor)

# Funções de percurso
print("Pre-Order:")
arvore.preOrder(raiz)
print("\n")

print("In-Order:")
arvore.inOrder(raiz)
print("\n")

print("Post-Order:")
arvore.postOrder(raiz)
print("\n")

print((arvore.busca(raiz, 20)).valor)

arvore.remocao(raiz, 25)
print (raiz.valor) #removemos a raiz agr printamos para ver qual é a nova raiz