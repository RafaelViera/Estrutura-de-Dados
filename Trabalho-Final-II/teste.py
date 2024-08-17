from TabelaHash import TabelaHash

tabela = TabelaHash(5)

tabela.inserir("casa")
tabela.inserir("cas")
tabela.inserir("ca")
tabela.inserir("c")

tabela.imprimirLista(0)
tabela.imprimirLista(2)
tabela.imprimirLista(3)
tabela.imprimirLista(4)
tabela.imprimirLista(5)