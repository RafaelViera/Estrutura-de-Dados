# Retorne a soma dos quadrados dos valores armazenados na lista. Se a lista estiver vazia, retorna
# o valor zero.

def somaAoQuadradoTotal(self):
    soma = 0
    if (self.prim == None):
        return 0
    p = self.prim
    while (p):
        soma += ((p.chave)*(p.chave))
        p = p.prox
    return soma