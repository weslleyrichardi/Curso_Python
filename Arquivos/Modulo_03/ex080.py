valores = list()
for posi in range(0, 5):
    digito = int(input("Digite um número: "))
    if posi == 0 or digito > valores[-1]:
        valores.append(digito)
        print("Final da lista.")
        print("—"*24)   
    else:
        posicao = 0
        while posicao < len(valores):
            if digito <= valores[posicao]:
                valores.insert(posicao, digito)
                print(f"Posição {posicao} da lista")
                print("—"*24)   
                break
            posicao += 1
print("—"*24)
print(valores)