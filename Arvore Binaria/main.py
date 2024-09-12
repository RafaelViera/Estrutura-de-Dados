from ArvoreBinaria import No
from ArvoreBinaria import ArvoreBinaria

arvore = ArvoreBinaria()

var = ""
while (var != "e"):
    var = input()

    if var == "i":
        palavra = input()
        arvore.inserirPalavra(palavra)
    
    elif var == "c":
        palavra = input()
        arvore.consultarPalavra(palavra)

    elif var == "f":
        arvore.palavrasMaisConsultadas()

    elif var == "o":
        letra1 = input()
        letra2 = input()
        arvore.ordemAlfabetica(letra1, letra2)

    elif var == "r":
        palavra = input()
        arvore.remove(palavra)

    elif var == "n": 
        nivel = input() 
        arvore.listarPalavrasNivel(nivel)

    elif var == "t":
        palavra = input()
        arvore.listarCaminho(palavra)

    elif var == "p":
        arvore.imprimirArvore()