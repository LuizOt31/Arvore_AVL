from arvore import no
from arvore import ArvoreAVL

arvore = ArvoreAVL()
raiz = None

raiz = arvore.insercao(raiz, 1)
raiz = arvore.insercao(raiz, 10)
raiz = arvore.insercao(raiz, 20)

print(raiz.chave)