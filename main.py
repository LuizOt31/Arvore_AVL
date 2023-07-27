from arvore import No
from arvore import ArvoreAVL

arvore = ArvoreAVL()
raiz = None

raiz = arvore.insercao(raiz, 100)
raiz = arvore.insercao(raiz, 20)
raiz = arvore.insercao(raiz, 30)

print(raiz.chave)
print(raiz.altura)

arvore.delete_node(raiz, 100)

arvore.busca(raiz, 100)