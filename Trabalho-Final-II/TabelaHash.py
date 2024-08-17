class NoHash:
    def __init__(self, chave):
        self.chave = chave
        self.numConsultas = 0
            
class TabelaHash:      
    def __init__(self, tamanho):
        self.tamanhoTabela = tamanho # tamanho total
        self.numElementos = 0 # quantidada de elementos salvo na tabela
        self.tabelaInterna = [[] for i in range(self.tamanhoTabela)]
    
    def somaOrdemLetras(self, palavra):          
        alfabeto = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
        'y', 'z'
        ]
        
        soma = 0
        for letra in palavra:
            soma= soma + self.buscaBinaria(alfabeto, letra) + 1
        return soma
    
    def buscaBinaria(self, lista, chave):
            dir = len(lista) - 1
            esq = 0
            
            while (esq <= dir):
                meio = int((esq + dir)/2)
                if lista[meio] == chave:
                    return meio
                if (chave < lista[meio]):
                    dir = meio - 1
                if (chave > lista[meio]):   
                    esq = meio + 1
    
    def funcaoH(self, chave): # Vulgo, função que retorna o indice p/ inserir
        return self.somaOrdemLetras(chave) % self.tamanhoTabela
    
    # 1 - "i" FEITO 
    def inserir(self, palavra):
        indice = self.funcaoH(palavra)
        
        # Verifica se à palavra já existe na lista
        for elemento in self.tabelaInterna[indice]:
            if elemento.chave == palavra:
                print(f"palavra ja existente: {palavra}") 
                return
        
        # Como não saio, palavra não existe na lista
        novoElemento = NoHash(palavra)
        self.tabelaInterna[indice].append(novoElemento)
        self.numElementos += 1
        print(f"palavra inserida: {palavra}")
        
    # 2 - "c" FEITO
    def consulta(self, palavra):
        indiceConsulta = self.funcaoH(palavra)
        
        # Verifica se a palavra está na lista
        for elemento in self.tabelaInterna[indiceConsulta]:
            if elemento.chave == palavra:
                elemento.numConsultas += 1
                print(f"palavra existente: {palavra} {elemento.numConsultas}")
                return
                
        print(f"palavra inexistente: {palavra}")
        
   # 5 - "r" ESTA COM ERRO NA LINHA DE REMOVER
    def remover(self, palavra):
        indiceRemover = self.funcaoH(palavra)
        
        for elemento in self.tabelaInterna[indiceRemover]:
            if elemento.chave == palavra:
                self.tabelaInterna.remove(indiceRemover)
                self.numElementos -= 1
                print(f"palavra removida: {palavra}")
                return
        
        print(f"palavra inexistente: {palavra}")

    # 6 - "n"
    def imprimirLista(self, n):
        print(f"palavras na entrada: {n}")
        if (len(self.tabelaInterna[n-1]) != 0):
            for elemento in self.tabelaInterna[n-1]:
                self.tabelaInterna[n-1].sort()
                print(elemento.chave)
        print(f"nao ha palavras na lista de indice: {n}")
    
    # 7 - "p"
    def imprimir(self):
        pass