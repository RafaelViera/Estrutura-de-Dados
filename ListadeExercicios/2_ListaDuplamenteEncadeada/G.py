# Retire o elemento de maior valor da lista

def removerMaiorElemento(self):
    if (self.prim == None):
        return False
    p, pMaior = self.prim
    maior = self.prim.chave
    while (p):
        if (p.chave > maior):
            maior = p.chave
            pMaior = p
        p = p.prox
    pMaior.ant.prox = pMaior.prox
    pMaior.prox.ant = pMaior.ant
    pMaior.prox = None
    pMaior.ant = None
    self.nelems -= 1
    return True