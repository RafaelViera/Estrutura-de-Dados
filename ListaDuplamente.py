from NoDuplo import NoDuplo

class ListaDuplamente:

    def __init__(self):
        self.head = NoDuplo()
        self.tail = NoDuplo()
        self.head.prox = self.tail
        self.tail.ant = self.head   

    def inserir(self, dado):
        NoNovo = NoDuplo(dado)
        p = self.tail.ant         # acho que fazer "self.tail.prox.ant = NoNovo" funcionaria
        p.prox = NoNovo           # mas coloquei um ponteiro pra ter certeza
        self.tail.ant = NoNovo  
        NoNovo.ant = p
        NoNovo.prox = self.tail
        
    def consulta():
        pass

    def remover():
        pass