def aumentar(valor = 0, porcem = 0):
    result = valor + (valor * porcem / 100)
    mais_taxa = result
    return mais_taxa


def diminuir(valor = 0, porcem = 0):
    result = valor - (valor * porcem / 100)
    menos_taxa = result
    return menos_taxa


def dobro(num = 0):
    result = 2 * num
    dobro = result
    return dobro
    
    
def metade(num = 0):
    result = num / 2
    metade = result
    
    return metade


def moeda(valor = 0, moeda= "R$"):
    formatado = f"{moeda}{valor:.2f}".replace(".", ",")
    
    return formatado
    
    