# Retire o elemento de maior valor da lista

def removerMaiorElemento(self):
    if (self.head.prox == self.tail):
        return False
    p = self.head.prox
    maior = self.head.prox.chave
    while (p):
        if (p.chave > maior):
            maior = p.chave
        p = p.prox
    maior.ant.prox = maior.prox
    maior.prox.ant = maior.ant
    maior.prox = None
    maior.ant = None