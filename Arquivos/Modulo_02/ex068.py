import random
soma = cont = 0
while True:
    opcao = input("\nPar ou impar? [P/I]: ").upper()
    jogador = int(input("Digite um número de 0 a 10: "))
    computador = random.randint(0, 10)
    soma = jogador + computador
    if opcao == "P":
        if soma % 2 == 0:
            print(f"\n{soma} é par, o jogador venceu.\n")
            cont += 1
        else:
            print("—"*50)
            break
    elif opcao == "I":
        if soma % 2 == 1:
            print(f"\n{soma} é impar, o jogador venceu.\n")
            cont += 1
        else:
            print("—"*50)
            break
    print("—"*50)
print(f"\nO resultado foi {soma}.\nO jogador venceu {cont} vezes consecutivas.")