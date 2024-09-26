from ListaSimplesmente import ListaSimplesmente
from ListaSimplesmente import NoLista

class No:
    def __init__(self, chave):
        self.chave = chave
        self.numConsultas = 0
        self.esq = None
        self.dir = None

class ArvoreBinaria:
    def __init__(self, dado=None, no=None):
        if no:
            self.raiz = no
        elif dado:
            no = No(dado)
            self.raiz = no
        else:
            self.raiz = None

    def inserirPalavra(self, palavra):
        if (self.buscar(palavra) is None):
            pai = None
            aux = self.raiz
            while (aux):
                pai = aux
                if palavra < aux.chave: 
                    aux = aux.esq
                else:
                    aux = aux.dir
            if pai is None:
                self.raiz = No(palavra)
            elif palavra < pai.chave:
                pai.esq = No(palavra)
            else:
                pai.dir = No(palavra)
            print(f"palavra inserida: {palavra}")
        else:
            print(f"palavra ja existente: {palavra}")

    def consultarPalavra(self, dado): 
        if self.raiz == None:
            return False
        if (self.buscar(dado) is None):
            print(f"palavra inexistente: {dado}")
            return False
        else:
            pont = self.raiz 
            while (pont.chave != dado): 
                if dado < pont.chave:
                    pont = pont.esq 
                else:
                    pont = pont.dir 
            pont.numConsultas += 1 # terminou o while já encontrou item   
            print(f"palavra existente: {dado} {pont.numConsultas}")
            return True
         
    def buscar(self, chave):
        if self.raiz == None:
            return None 
        atual = self.raiz 
        while atual.chave != chave: 
            if chave < atual.chave:
                atual = atual.esq 
            else:
                atual = atual.dir 
            if atual == None:
                return None 
        return atual  
    
    def palavrasMaisConsultadas(self):
        if (self.raiz is None):
            print("arvore vazia")
            return

        palavras = ListaSimplesmente()

        def percorrer(no, maxConsultas):
            if no is None:
                return maxConsultas
            
            maxConsultas = percorrer(no.esq, maxConsultas)
            
            if no.numConsultas > maxConsultas:
                maxConsultas = no.numConsultas
                palavras.prim = NoLista(no.chave)
                palavras.nelems = 1
            elif no.numConsultas == maxConsultas:
                palavras.inserir(no.chave)
            
            return percorrer(no.dir, maxConsultas)

        maxConsultas = percorrer(self.raiz, 0)

        print("palavras mais consultadas:")
        palavras.imprimirLista()
        print(f"numero de acessos: {maxConsultas}")

    def ordemAlfabetica(self, l1, l2):
        ordem = ListaSimplesmente()

        def emOrdem(no, l1, l2):
            if no:
                emOrdem(no.esq, l1, l2)
                if (l1 <= no.chave <= l2) or (l1 == no.chave[0] or l2 == no.chave[0]):
                    ordem.inserirEmOrdem(no.chave)
                emOrdem(no.dir, l1, l2)

        emOrdem(self.raiz, l1, l2)

        if ordem.nelems == 0:
            print("lista vazia")
        else:
            print("palavras em ordem:")
            ordem.imprimirLista()

    def remover(self, palavra):
        no = self.buscar(palavra)
        if no is None:
            print(f'palavra inexistente: {palavra}')
        else:
            self.raiz = self._remover(self.raiz, palavra)
            print(f'palavra removida: {palavra}')

    def _remover(self, no, palavra):
        if no is None:
            return no

        if palavra < no.chave:
            no.esq = self._remover(no.esq, palavra)
        elif palavra > no.chave:
            no.dir = self._remover(no.dir, palavra)
        else:
            if no.esq is None:
                return no.dir
            elif no.dir is None:
                return no.esq
            aux = self.minNo(no.dir)
            no.chave = aux.chave
            no.numConsultas = aux.numConsultas
            no.dir = self._remover(no.dir, no.chave)
        return no

    def min(self, node=None):
        if node == None:
            node = self.raiz
        while node.esq:
            node = node.dir
        return node.chave
    
    def minNo(self, no):
        aux = no
        while aux.esq is not None:
            aux = aux.esq
        return aux

    def listarCaminho(self, palavra):
        caminho = ListaSimplesmente()
        existe = self._listarCaminho(self.raiz, palavra, caminho)
        
        if existe:
            print("Palavras no caminho:")
            caminho.imprimirLista()
        else:
            print(f"Palavra inexistente: {palavra}")

    def _listarCaminho(self, no, palavra, caminho):
        if no is None:
            return False
        caminho.inserirEmOrdem(no.chave)
        if no.chave == palavra:
            return True
        elif palavra < no.chave:
            if self._listarCaminho(no.esq, palavra, caminho):
                return True
        else:
            if self._listarCaminho(no.dir, palavra, caminho):
                return True
        return False

    def imprimirArvore(self):
        if self.raiz is None:
            print("arvore vazia")
        else:
            self._imprimirArvore(self.raiz)

    def _imprimirArvore(self, no):
        if (no is not None):
            if (no.esq is not None):
                esq_str = no.esq.chave
            else:
                esq_str = "nill"
            
            if (no.dir is not None):
                dir_str = no.dir.chave
            else:
                dir_str = "nill"
                
            print(f"palavra: {no.chave} freq: {no.numConsultas} fesq: {esq_str} fdir: {dir_str}")
            
            self._imprimirArvore(no.esq)
            self._imprimirArvore(no.dir)