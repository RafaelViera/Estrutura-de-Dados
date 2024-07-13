# Retorne a media dos valores na lista. Se a lista estiver vazia, a media deve ser considerada zero.

def media(self):
    soma, media, cont = 0
    if (self.head.prox == self.tail):
        return media
    p = self.head.prox
    while (p):
        soma += p.chave
        cont += 1
        p = p.prox
    media = (soma / cont)
    return media