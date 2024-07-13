# Retorne o menor elemento da lista. Se a lista nao tiver elementos, a funcao deve retornar uma
# indicacao de que a lista esta vazia.

def menorElemento(self):
    if (self.prim == None):
        return ("A lista está vazia")
    p = self.prim
    menor = self.prim.chave
    while (p):
        if (p.chave < menor):
            menor = p.chave
        p= p.prox
    return menor