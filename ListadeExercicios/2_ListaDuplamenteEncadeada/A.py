# Retorne o menor elemento da lista. Se a lista nao tiver elementos, a funcao deve retornar uma
# indicacao de que a lista esta vazia.

def menorElemento(self):
    if (self.prim == None):
        return -1
    p = p.prim
    menor = p.prim.chave
    while (p):
        if (p.chave < menor):
            menor = p.chave
        p = p.prox
    return menor