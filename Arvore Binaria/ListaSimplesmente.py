class NoLista:
    def __init__(self, x):
        self.chave= x
        self.prox= None

class ListaSimplesmente:
    def __init__(self):
        self.prim= None
        self.nelems= 0

    def inserir(self, x):
        if (self.prim != None):
            p = self.prim
            while (p.prox):
                p = p.prox
            p.prox = NoLista(x)
        else:
            self.prim = NoLista(x)
        self.nelems += 1

    def consulta(self, x):
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
            
    def imprimirLista(self):
        p = self.prim
        while (p != None):
            print(p.chave)
            p = p.prox