PARAR = False
núm = maior = menor = media = soma = cont = 0
while not PARAR:
    núm = int(input("Digite um número: "))
    soma += núm
    if not PARAR:
        cont += 1
    if cont == 1:
        maior = menor = núm
    if núm > maior:
        maior = núm
    elif núm < menor:
        menor = núm
    flag = input("Deseja continuar? [S/N]: ")
    if flag in 'Nn ':
        PARAR = True
media = soma / cont
print(f'\nO maior número foi {maior}\nMenor número foi {menor}\nA media dos {cont} números foi {media:.2f}\nA soma de todos foi {soma}')
