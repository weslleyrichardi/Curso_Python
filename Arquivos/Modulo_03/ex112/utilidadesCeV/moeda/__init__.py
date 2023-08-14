def moeda(valor=0, moeda="R$"):
    formatado = f"{moeda}{valor:.2f}".replace(".", ",")

    return formatado


def aumentar(valor=0, porcem=0, format=False):
    result = valor + (valor * porcem / 100)
    return result if format is False else moeda(result)


def diminuir(valor=0, porcem=0, format=False):
    result = valor - (valor * porcem / 100)
    return result if format is False else moeda(result)


def dobro(num=0, format=False):
    result = 2 * num
    return result if format is False else moeda(result)


def metade(num=0, format=False):
    result = num / 2
    return result if format is False else moeda(result)


def resumo(preco=0, aumento=0, diminui=0):
    print("—"*30)
    print(f" RESUMO DO VALOR".center(30))
    print(''+"—"*30)
    print(f" Preço analisado: \t{moeda(preco)}")
    print(f" Dobro do Preço: \t{dobro(preco, True)}")
    print(f" Metade do preço: \t{metade(preco, True)}")
    print(f" {aumento}% de aumento: \t{aumentar(preco, aumento, True)}")
    print(f" {diminui}% de redução: \t{diminuir(preco, diminui, True)}")
    print(''+"—"*30)