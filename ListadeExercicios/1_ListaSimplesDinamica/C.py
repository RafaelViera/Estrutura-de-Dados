# Retorne a media dos valores na lista. Se a lista estiver vazia, a media deve ser considerada zero.

def media(self):
    soma, media, cont = 0
    if (self.prim == None):
        return media
    p = self.prim
    while (p):
        soma += p.chave
        aux += 1
        p = p.prox
    media = (soma / cont)
    return media
