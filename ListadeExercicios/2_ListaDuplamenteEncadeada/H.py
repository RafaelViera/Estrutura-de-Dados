#Retire todos os elementos da lista com chave igual a um valor x, passado como parametro. Para
#esta questao, considere que a lista pode conter mais de um elemento com mesmo valor de chave.

def retirarElementosIguais(self, x):
    if (self.head.prox == self.tail):
        return False
    p = self.head.prox
    while (p):
        if (p.chave == x):
            p.ant.prox = p.prox
            p.prox.ant = p.ant
            p.prox = None
            p.ant = None
        p = p.prox
    return True