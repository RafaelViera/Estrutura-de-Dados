# Elimine o k-esimo elemento da lista, se houver. Considere que o primeiro elemento da lista esta
# na posicao 1.

def removerElemento(self, k_esimo):
    if (self.prim == None):
        return ("A lista esta vazia")
    p, p_ant = self.prim
    for i in range(k_esimo):
        if (i == 0):
            p = p.prox
        elif (i == k_esimo):
            p_ant.prox = p.prox
            p.prox = None
            return True
        else:
            p = p.prox
            p_ant = p_ant.prox
    return False