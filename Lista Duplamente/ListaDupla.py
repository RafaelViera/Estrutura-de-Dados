from NoDuplo import NoDuplo

class ListaDuplamente:
    def __init__(self):
        self.prim = None
        self.nelems= 0 

    def inserir(self, dado):
        # Insere depois do ultimo elemento
        if (self.prim !=  None):
            p = self.prim
            while (p.prox):
                p = p.prox
            p.prox = NoDuplo(dado)
            p.prox.ant = p
        else:
            self.prim = NoDuplo(dado)
        self.nelems += 1

    def consulta(self, dado):
        # Retonar o indice que o elemento está
        if (self.prim == None):
            return -1
        p = self.prim
        indice = 0
        while (p):
            if (p.chave == dado):
                return indice
            p = p.prox
            indice += 1
        return -1

    def remover(self, dado):
        # Caso a lista esteja vazia
        if (self.prim == None):
            return False
        # Caso o dado seja o primeiro da lista
        elif (self.prim.chave == dado):
            self.prim = self.prim.prox
            self.nelems -= 1
            return True
        else:
            p = self.prim
            while (p):
                if (p.chave == dado):
                    p.ant.prox = p.prox
                    p.prox.ant = p.ant
                    self.nelems -= 1
                    return True
                p = p.prox
        return False
    
    def imprimir(self):
        # Mostra a lista na ordem de inserção
        p = self.prim
        while (p):
            print(p.chave)
            p = p.prox