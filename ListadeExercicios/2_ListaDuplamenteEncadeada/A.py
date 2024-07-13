# Retorne o menor elemento da lista. Se a lista nao tiver elementos, a funcao deve retornar uma
# indicacao de que a lista esta vazia.

def menorElemento(self):
    if (self.head.prox == self.tail):
        return ("A lista esta vazia")
    p = self.head.prox
    menor = self.head.prox.chave
    while (p):
        if (menor > p.chave):
            menor = p.chave
        p = p.prox
    return menor