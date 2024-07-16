#Retire todos os elementos da lista com chave igual a um valor x, passado como parametro. Para
#esta questao, considere que a lista pode conter mais de um elemento com mesmo valor de chave.

def retirarElementosIguais(self, x):
    if (self.prim == None):
        return False
    p = self.prim
    while (p):
        if (p.chave == x):
            p.ant.prox = p.prox
            p.prox.ant = p.ant
            p.prox = None
            p.ant = None
            self.nelems -= 1
        p = p.prox
    return True