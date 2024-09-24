class NoHash:
    def __init__(self, chave):
        self.chave = chave
        self.numConsultas = 0
            
class TabelaHash:      
    def __init__(self, tamanho):
        self.tamanhoTabelaInterna = tamanho # tamanho total
        self.numElementos = 0 # quantidada de elementos salvo na tabela
        self.tabelaInterna = [[] for i in range(self.tamanhoTabelaInterna)]
    
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
            elif (chave < lista[meio]):
                dir = meio - 1
            else: 
                esq = meio + 1
    
    # Vulgo, função que retorna o indice de onde inserir
    def funcaoH(self, chave):
        return self.somaOrdemLetras(chave) % self.tamanhoTabelaInterna
    
    def inserir(self, palavra):
        indice = self.funcaoH(palavra)
        
        # Verifica se à palavra já existe na lista
        for elemento in self.tabelaInterna[indice]:
            if elemento.chave == palavra:
                print(f"palavra ja existente: {palavra}") 
                return False
        
        # Como não saiu, palavra não existe na lista
        novoElemento = NoHash(palavra)
        self.tabelaInterna[indice].append(novoElemento)
        self.numElementos += 1
        print(f"palavra inserida: {palavra}")
        
    def consulta(self, palavra):
        indiceConsulta = self.funcaoH(palavra)
        
        # Verifica se a palavra está na lista
        for elemento in self.tabelaInterna[indiceConsulta]:
            if elemento.chave == palavra:
                elemento.numConsultas += 1
                print(f"palavra existente: {palavra} {elemento.numConsultas}")
                return True
                
        print(f"palavra inexistente: {palavra}")
        return False
        
    def maisConsultada(self):
        # Verifica se a lista esta vazia
        if (self.numElementos == 0):
            print("tabela vazia")
            return False
        
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
        for palavra in palavrasMaisConsultadas:
            print(palavra)
        print(f"numero de acessos: {maiorNumConsulta}")
        
    def imprimirOrdemAlfabetica(self, l1, l2):
        # Coleta todas as palavras da tabela
        palavrasTodas = []
        for lista in self.tabelaInterna:
            palavrasTodas.extend(lista)

        # Filtra palavras que começam com letras entre l1 e l2, inclusive os proprios
        palavrasSelecionadas = []
        for palavra in palavrasTodas:
            if (l1 <= palavra.chave <= l2) or (l1 == palavra.chave[0] or l2 == palavra.chave[0]):
                palavrasSelecionadas.append(palavra)
        
        #Ordena de forma alfabetica em uma nova lista as palavras selecionadas
        palavrasOrdenadas = sorted(palavrasSelecionadas, key=lambda x: x.chave)
        
        if palavrasOrdenadas:
            print(f"palavras em ordem: ")
            for palavra in palavrasOrdenadas:
                print(palavra.chave)
        else:
            print("não há palavras nesse intervalo")
                    
    def remover(self, palavra):
        indiceRemover = self.funcaoH(palavra)

        # Verifica se a palavra está na lista então remove
        for elemento in self.tabelaInterna[indiceRemover]:
            if elemento.chave == palavra:
                self.tabelaInterna[indiceRemover].remove(elemento) 
                self.numElementos -= 1
                print(f"palavra removida: {palavra}")
                return True

        print(f"palavra inexistente: {palavra}")
        return False
        
    def imprimirLista(self, n):
        palavras = self.tabelaInterna[int(n)]
        
        if palavras:
            print(f"palavras na entrada: {n}")
            for palavra in palavras:
                print(palavra)
        else:
            print(f"nao ha palavras na lista de indice: {n}")
    
    def imprimirTabela(self):
        for i in range(self.tamanhoTabelaInterna):
            print(f"{i}: ", end="")  
            palavras = self.tabelaInterna[i]
           
            for elemento in palavras:
                print(f"{elemento.chave} {elemento.numConsultas} ", end="")
            print()  # Nova linha para o próximo índice