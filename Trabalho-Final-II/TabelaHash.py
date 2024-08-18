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
        
    # 3 - "f" FEITO
    def maisConsultada(self):
        # Verifica se a lista esta vazia
        if (self.numElementos == 0):
            print("tabela vazia")
            return
        
        # Mais consultadas
        palavrasMaisConsultadas = []
        maiorNumConsulta = 0
        for lista in self.tabelaInterna:
            for elemento in lista:
                if (elemento.numConsultas > maiorNumConsulta):
                    palavrasMaisConsultadas = []
                    palavrasMaisConsultadas.append(elemento.chave)
                    maiorNumConsulta = elemento.numConsultas
                elif (elemento.numConsultas == maiorNumConsulta):
                    palavrasMaisConsultadas.append(elemento.chave)

        # Quando saiu dos loop's temos a lista com as palavras mais consultadas
        palavrasMaisConsultadas.sort()
        for palavra in palavrasMaisConsultadas:
            print(palavra)
        print(f"numero de acessos: {maiorNumConsulta}")
        
    # 4 - "o" FEITO
    def imprimirOrdemAlfabetica(self, l1, l2):
        # Coleta todas as palavras da tabela
        palavrasFiltradas = []
        for lista in self.tabelaInterna:
            palavrasFiltradas.extend(lista)

        # Filtra palavras que começam com letras entre l1 e l2, inclusive
        palavrasSelecionadas = [palavra for palavra in palavrasFiltradas if (l1 <= palavra.chave <= l2) or (l1 == palavra.chave[0] or l2 == palavra.chave[0])]
        
        print(f"palavras em ordem: ")
        if palavrasSelecionadas:
            for palavra in palavrasSelecionadas:
                print(palavra.chave)
        else:
            print("lista vazia")
                    
    # 5 - "r" ESTA COM ERRO NA LINHA DE REMOVER
    def remover(self, palavra):
        indiceRemover = self.funcaoH(palavra)
        
        for elemento in self.tabelaInterna[indiceRemover]:
            if elemento.chave == palavra:
                self.tabelaInterna[indiceRemover].remove(indiceRemover)
                self.numElementos -= 1
                print(f"palavra removida: {palavra}")
                return
        
        print(f"palavra inexistente: {palavra}")
    
    # 5 - "r" ESTA COM ERRO 
    def removerPalavra(self, palavra):
        indice = self.funcaoH(palavra)

        if palavra in self.tabelaInterna[indice]:
            self.tabelaInterna[indice].remove(palavra)
            print(f'palavra removida: {palavra}')
            self.numElementos -= 1 
        else:
            print(f'palavra inexistente: {palavra}')

    # 6 - "n" FEITO
    def imprimirLista(self, n):
        palavras = self.tabelaInterna[n]
        
        if palavras:
            print(f"palavras na entrada: {n}")
            palavrasOrdenadas = sorted(elemento.chave for elemento in palavras)
            for palavra in palavrasOrdenadas:
                print(palavra)
        else:
            print(f"nao ha palavras na lista de indice: {n}")
    
    # 7 - "p" FEITO
    def imprimirTabela(self):
        for i in range(self.tamanhoTabela):
            print(f"{i}: ", end="")  
            palavras = self.tabelaInterna[i]
           
            palavrasOrdenadas = sorted(palavras, key=lambda x: x.chave)
            for elemento in palavrasOrdenadas:
                print(f"{elemento.chave} {elemento.numConsultas} ", end="")
            print()  # Nova linha para o próximo índice