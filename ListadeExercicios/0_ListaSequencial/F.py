# Elimine o k-esimo elemento da lista, se houver. Considere que o primeiro elemento da lista esta
# na posicao 1.

def removerElemento(self, k_esimo):
    if (self.nelems == 0):
        return ("A lista esta vazia")
    if (k_esimo < len(self.dados)):
        self.dados[k_esimo - 1] = 0
        self.nelems -= 1
    else:
        return False