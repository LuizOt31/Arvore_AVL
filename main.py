from AVLTree import No
from AVLTree import ArvoreAVL

def main():
    # Criacao uma árvore vazia
    arvore = ArvoreAVL()

    # Inserindo os elementos na árvore
    raiz = None
    elementos = [1, 10, 20]
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

if __name__ == "__main__":
    main()
