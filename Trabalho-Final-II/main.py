from TabelaHash import TabelaHash

tabela = TabelaHash(10)

var = ""
while (var != "e"):
    var = input()

    if var == "i":
        palavra = input()
        tabela.inserir(palavra)
    
    elif var == "c":
        palavra = input()
        tabela.consulta(palavra)

    elif var == "f":
        tabela.maisConsultada()

    elif var == "o":
        letra1 = input()
        letra2 = input()
        tabela.imprimirOrdemAlfabetica(letra1, letra2)

    elif var == "r":
        palavra = input()
        tabela.remover(palavra)

    elif var == "n": 
        nivel = input() 
        tabela.imprimirLista(nivel)

    elif var == "p":
        tabela.imprimirTabela()
    
    elif var == "e":
        break