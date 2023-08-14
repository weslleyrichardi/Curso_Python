# ex 107
def aumentar(valor, porcem):
    result = valor + (valor * porcem / 100)
    mais_taxa = result
    return mais_taxa


def diminuir(valor, porcem):
    result = valor - (valor * porcem / 100)
    menos_taxa = result
    return menos_taxa


def dobro(num):
    result = 2 * num
    dobro = result
    return dobro
    
    
def metade(num):
    result = num / 2
    metade = result
    return metade


# ex 108
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
    
    
# ex 109
def moeda(valor = 0, moeda= "R$"):
    formatado = f"{moeda}{valor:.2f}".replace(".", ",")
    
    return formatado
    
def aumentar(valor = 0, porcem = 0, format = False):
    result = valor + (valor * porcem / 100)
    return result if format is False else moeda(result)


def diminuir(valor = 0, porcem = 0, format = False):
    result = valor - (valor * porcem / 100)
    return result if format is False else moeda(result)


def dobro(num = 0, format = False):
    result = 2 * num
    return result if format is False else moeda(result)

    
def metade(num = 0, format = False):
    result = num / 2
    return result if format is False else moeda(result)

