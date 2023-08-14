def escreva(txt):
    tamanho = len(txt) + 4
    print(" "+"-"*tamanho)
    print(" | "+txt+" | ")
    print(" "+"-"*tamanho)


escreva(str(input("Digite uma frase: ")))
