class NoLista:
    def __init__(self, x):
        self.chave= x
        self.prox= None

class ListaSimplesmente:
    def __init__(self):
        self.prim= None
        self.nelems= 0

    def inserir(self, x):
        if (self.prim== None):
            self.prim= NoLista(x)
        p= self.prim
        while (p.prox):
            p= p.prox
        p.prox= NoLista(x)
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
       if ( self.prim == None): # caso a lista esteja vazia
           return False
       elif ( self.prim == x):  # se o elemente procurado é o primeiro da lista
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
       return (False)           # caso o elemento nem esteja na lista
    
    
    ### Funções de apoio a classe Arvore Binaria ###

    def inserirEmOrdem(self, chave):
        novoNo = NoLista(chave)
        if (self.prim is None) or (self.prim.chave > chave):
            novoNo.prox = self.prim
            self.prim = novoNo
        else:
            atual = self.prim
            while (atual.prox is not None) and (atual.prox.chave < chave):
                atual = atual.prox
            novoNo.prox = atual.prox
            atual.prox = novoNo    
        self.nelems += 1

    def imprimirSequencia(self):
        atual = self.prim
        while (atual is not None):
            print(atual.chave)
            atual = atual.prox
            
    def imprimirLista(self):
        p = self.prim
        while p:
            print(p.chave)
            p = p.prox