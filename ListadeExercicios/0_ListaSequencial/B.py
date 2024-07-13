# Retorne o numero de elementos com chave ımpar na lista.

def chavesImpar(self):
    if (self.nelems == 0):
        return ("A lista esta vazia")
    quantidadeImpar = 0
    for i in range(len(self.dados)):
        if ((self.dados[i] % 2) != 0):
            quantidadeImpar += 1
    return quantidadeImpar