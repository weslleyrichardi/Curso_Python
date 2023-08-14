while True:
    valor = int(input("Digite um valor para a tabuada: "))
    if valor < 0:
        break
    print("—"*25)
    for cont in range(1, 11):
        print(f'{cont} × {valor} = {cont * valor}')
    print("—"*25)
print("—"*52)
print(f'O programa foi encerrado porque (\033[31m {valor} \033[m) é negativo. |')