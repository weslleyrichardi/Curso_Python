def fatorial(numero, show = False):
    print("_"*30)
    indice=1
    for fator in range(numero, 0, -1):
        indice *= fator
        if show:
            if fator != 1:
                print(fator, end=" × ")
            if fator == 1:
                print(fator, end=" = ")
    return indice
        
    
print(fatorial(5, show = True))

help(fatorial)