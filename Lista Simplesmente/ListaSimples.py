from NoSimples import No

class ListaSimplesmente:
    def __init__(self):
        self.prim= None
        self.nelems= 0

    def inserir(self, x):
        # Insere depois do ultimo elemento
        if (self.prim != None):
            p = self.prim
            while (p.prox):
                p = p.prox
            p.prox = No(x)
        else:
            self.prim = No(x)
        self.nelems += 1

    def consulta(self, x):
        # Retonar o indice que o elemento está
        p= self.prim
        i= 0
        while (p):
            if (p.chave == x):
                return i
            p= p.prox
            i= i + 1
        return -1
    
    def remover(self, x):
        # Caso a lista esteja vazia
        if (self.prim == None):
            print('entrou0')
            return False
        # Se o elemente procurado é o primeiro da lista
        elif (self.prim.chave == x):
            self.prim = self.prim.prox
            self.nelems = self.nelems - 1
            return True
        else:
            p = self.prim.prox
            pant = self.prim
            while (p):
                if (p.chave == x):
                    pant.prox = p.prox
                    p.prox = None
                    self.nelems= self.nelems - 1
                    return True
                else:
                    pant = p
                    p = p.prox
        # Caso o elemento nem esteja na lista
        return (False)
   
    def imprimir(self):
        # Print em ordem de inserção
        if (self.prim == None):
            return False
        p = self.prim
        while (p):
            print(p.chave)
            p = p.prox