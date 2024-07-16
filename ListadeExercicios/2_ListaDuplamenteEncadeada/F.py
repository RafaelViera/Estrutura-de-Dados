# Elimine o k-esimo elemento da lista, se houver. Considere que o primeiro elemento da lista esta
# na posicao 1.

def removerElemento(self, k_esimo):
    if (self.prim == None):
        return False
    p = self.prim
    for i in range(1, k_esimo + 1):
        if (k_esimo == i):
            p.ant.prox = p.prox
            p.prox.ant = p.ant
            p.prox =  None
            p.ant = None
            self.nelems -= 1
            return True
        p = p.prox
    return False