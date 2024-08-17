from TabelaHash import TabelaHash

tabela = TabelaHash(12)

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
        pass

    elif var == "o":
        letra1 = input()
        letra2 = input()
        pass

    elif var == "r":
        palavra = input()
        pass

    elif var == "n": 
        nivel = input() 
        pass

    elif var == "t":
        palavra = input()
        pass
    
    elif var == "e":
        break