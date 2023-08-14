N = soma = cont = 0
parar = False
while not parar:
    N = int(input("Digite um número: "))
    if N== 999:
        parar = True
    else:
        soma += N
        cont += 1
print(f"A soma é {soma} e você digitou {cont} números.")
