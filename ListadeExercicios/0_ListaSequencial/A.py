# Retorne o menor elemento da lista. Se a lista nao tiver elementos, a funcao deve retornar uma
# indicacao de que a lista esta vazia.

def menorElemento(self):
    if (self.nelems == 0):
        return ("A lista esta vazia")
    menorElemento = self.dados[0]
    for i in range (len(self.dados)):
        if (self.dados[i] < menorElemento):
            menorElemento = self.dados[i]
    return menorElemento