# Retorna a soma dos valores armazenados na lista. Se a lista estiver vazia, retorna o valor zero.

def somaTotal(self):
    soma = 0
    if (self.head.prox == self.tail):
        return 0
    p = self.head.prox
    while (p):
        soma += p.chave
        p = p.prox
    return soma