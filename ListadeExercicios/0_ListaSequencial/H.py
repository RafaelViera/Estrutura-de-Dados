# Retire todos os elementos da lista com chave igual a um valor x, passado como paremetro. A lista pode ter mais de um elemento com a mesma chave.

def removerIguais(self, chave):
    if (self.nelems == 0):
        return ("A lista esta vazia")
    for i in range(len(self.dados)):
        if (self.dados[i] == chave):
            self.dados[i] = 0
            self.nelems -= 1