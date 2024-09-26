from ListaDupla import ListaDuplamente

lista = ListaDuplamente()

lista.inserir(10)
lista.inserir(20)
lista.inserir(30)
lista.inserir(40)
lista.inserir(50)

lista.remover(30)
lista.remover(40)

print(lista.consulta(40))

lista.imprimir()

lista.inserir(40)

print(lista.consulta(40))

lista.imprimir()