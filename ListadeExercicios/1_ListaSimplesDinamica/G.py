# Retire o elemento de maior valor da lista

# TODO VERIFICAR SE AINDA TEM ALGUM ERRO NO ALGORITMO

def removerMaiorElemeno(self):
    if (self.prim == None):
        return ("A lista está vazia")
    p = self.prim.prox
    p_ant = self.prim
    maior = self.prim.chave
    while (p_ant):
        if (p_ant.chave > maior):
            maior = p_ant
        else:
            p = p.prox
            p_ant = p_ant.prox
    p_ant.prox = maior.prox
    maior.prox = None