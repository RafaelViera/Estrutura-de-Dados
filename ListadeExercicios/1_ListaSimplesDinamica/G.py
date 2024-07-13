# Retire o elemento de maior valor da lista

def removerMaiorElemeno(self):
    if (self.prim == None):
        return ("A lista está vazia")
    p = self.prim
    maior = self.prim.chave
    while (p):
        if (p.chave > maior):
            maior = p.chave
        p = p.prox