class ListaEstatica:
    def  __init__ ( self, nmax):
        self.dados=[0]*nmax
        self.nelems= 0

    def inserir(self, x):
        if ( len(self.dados) == self.nelems):
            return False
        self.dados[self.nelems]= x
        self.nelems += 1
        return True
    
    def consulta( self, x):
        if ( self.nelems == 0):
            return False
        cont= 0
        while ( cont <= self.nelems):
            if ( self.dados[cont] == x):
                return True
            cont= cont + 1
        return False
    
    def remover( self, x):
        if ( self.nelems == 0):
            return False
        cont= 0
        while ( cont <= self.nelems):
            if ( self.dados[cont] == x):
                self.dados[cont]=0
                self.nelems -= 1
            cont= cont + 1
        return False