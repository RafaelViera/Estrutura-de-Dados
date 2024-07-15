# Retire o elemento de maior valor da lista

def removerMaiorElemento(self):
    if (self.head.prox == self.tail):
        return False
    p = self.head.prox
    pMaior = self.head.prox
    maior = self.head.prox.chave
    while (p):
        if (p.chave > maior):
            maior = p.chave
            pMaior = p
        p = p.prox
    pMaior.ant.prox = pMaior.prox
    pMaior.prox.ant = pMaior.ant
    pMaior.prox = None
    pMaior.ant = None
    return True