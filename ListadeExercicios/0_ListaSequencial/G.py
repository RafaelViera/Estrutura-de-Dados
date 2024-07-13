# Retire o elemento de maior valor da lista

def removerMaiorElemeno(self):
    if (self.nelems == 0):
        return ("A lista esta vazia")
    maior = self.dados[0]
    aux = 0
    for i in range(len(self.dados)):
        if (self.dados[i] > maior):
            maior = self.da[i]
            aux = i
    self.dados[i] = 0
    self.nelems -= 1