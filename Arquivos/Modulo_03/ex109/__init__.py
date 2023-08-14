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

