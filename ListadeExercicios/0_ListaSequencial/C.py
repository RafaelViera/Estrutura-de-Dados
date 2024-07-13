# Retorne a media dos valores na lista. Se a lista estiver vazia, a media deve ser considerada zero.

def media(self):
    soma, media = 0
    if (self.nelems == 0):
        return media
    for i in range(len(self.dados)):
        soma += self.dados[i]
    media = (soma / self.nelems)
    return media