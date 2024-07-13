# Retorna a soma dos valores armazenados na lista. Se a lista estiver vazia, retorna o valor zero.

def somaTotal(self):
    soma = 0
    if (self.nelems == 0):
        return 0
    for i in range(len(self.dados)):
        soma += self.dados[i]
    return soma
