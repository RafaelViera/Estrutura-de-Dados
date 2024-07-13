# Retorne o numero de elementos com chave ımpar na lista.

def chavesImpar(self):
    if (self.head.prox == self.tail):
        return ("A lista esta vazia")
    quantidadeImpar = 0
    p = self.head
    while (p):
        if ((p.chave % 2) != 0):
            quantidadeImpar += 1
        p = p.prox
    return quantidadeImpar