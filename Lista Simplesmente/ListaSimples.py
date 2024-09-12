from NoSimples import No

class ListaSimplesmente:
    def __init__(self):
        self.prim= None
        self.nelems= 0

    def inserir(self, x):
        if (self.prim== None):
            self.prim= No(x)
        p= self.prim
        while (p.prox):
            p= p.pro
        p.prox= No(x)
        self.nelems= self.nelems + 1

    def consulta(self, x):
        p= self.prim
        i= 0
        while (p):
            if (p.chave == x):
                return (True, i)
            p= p.prox
            i= i + 1
        return (False)
    
    def remover(self, x):
       # caso a lista esteja vazia
       if ( self.prim == None):
           return False
       # se o elemente procurado é o primeiro da lista
       elif ( self.prim == x):
           self.prim= self.prim.prox
           self.nelems= self.nelems - 1
           return (True)
       else:
           p= self.prim.prox
           pant= self.prim
           while (p):
               if ( p.chave == x):
                   pant= p.prox
                   p.prox= None 
               pant= pant.prox
               p= p.prox
               self.nelems= self.nelems - 1
        # caso o elemento nem esteja na lista
       return (False)