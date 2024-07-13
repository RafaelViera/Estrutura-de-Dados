from NoDuplo import NoDuplo

class ListaDuplamente:

    def __init__(self):
        self.head = NoDuplo()
        self.tail = NoDuplo()
        self.head.prox = self.tail
        self.tail.ant = self.head   

    def inserir(self, dado):
        NoNovo = NoDuplo(dado)
        NoNovo.ant = self.head
        NoNovo.prox = self.tail
        self.head.prox = NoNovo
        self.tail.ant = NoNovo
        
    def consulta():
        pass

    def remover():
        pass