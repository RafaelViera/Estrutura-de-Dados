# Retorne o numero de elementos com chave ımpar na lista.

def chavesImpar(self):
    if (self.prim == None):
        return 0
    quantidadeImpar = 0
    p = self.prim
    while (p):
        if ((p.chave % 2) != 0):
            quantidadeImpar += 1
        p = p.prox
    return quantidadeImpar