from NoDuplo import NoDuplo

class ListaDuplamente:

    def __init__(self):
        self.prim = None
        self.nelems= 0 

    def inserir(self, dado):
        if (self.prim ==  None):
            No = NoDuplo(dado)
            self.prim = No
        p = self.prim
        while(p):
            if (self.prim == No):
                self.prim = NoDuplo(dado)
            p = p.prox
            self.nelems = self.nelems + 1

    def consulta(self, dado):
        if (self.prim == None):
            return (False)
        p = self.prim
        aux = 0
        while (p):
            if (p.chave == dado):
                return (True, aux)
            p = p.chave
        return (False)

    def remover(self, dado):
        if (self.prim == None):
             return False
        elif (self.prim.chave == dado):
             self.prim == self.prim.prox
             self.nelems -= 1
             return True
        else:
             p = self.prim
             while (p):
                if (p.chave == dado):
                    p.ant.prox = p.prox
                    p.prox.ant = p.ant
                    p.prox = None
                    p.ant = None
                    self.nelems -= 1
                    return True
                p = p.prox
        return False