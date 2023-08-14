def maior(*valores):
    maior = cont = 0
    for valor in valores:
        print(valor, end=" - ")
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
        
    print("Fim!")
    print(f"O maior valor foi {maior}.")


maior(19, 2, 1, 6, 9, 0)
