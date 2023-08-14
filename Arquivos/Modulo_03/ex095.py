gols = list()
jogador = dict()
time = []
while True:
    jogador.clear()
    gols.clear()
    nome = str(input("Nome: "))
    partidas = int(input("Quantidade de partidas jogadas: "))
    for partida in range(1, partidas+1):
        gols.append(int(input(f"Gols na partida {partida+1}: ")))
    jogador = {'Nome':nome, 'Partidas':partidas, 'gols': gols[:],'Gols': sum(gols)}
    time.append(jogador.copy())
    while True:
        resp = str(input("Deseja continuar?: ")).upper()[0]
        if resp in 'SN':
            break
        print("\033[31mERRO!\033[m Porfavor digite \033[32mS\033[m ou \033[32mN\033[m")
    if resp in 'N':
        break

print(f"Cod  ", end="")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
print("="*60)
for k, v in enumerate(time):
    print(f"{k:>4} ", end="")
    for dado in v.values():
        print(f"{str(dado):<15}", end='')
    print()
print("="*60)

while True:
    busca = int(input("Digite o código do jogador (999 para parar): "))
    print("="*50)
    if busca == 999:
        break
    if busca >= len(time):
        print("\033[31mERRO!\033[m não existe jogador com o codigo {busca}. Porfabor digite um código válido.")
    else:
        print(f"Levantamento do jogador {time[busca]['Nome']}")
        for i, v in enumerate(time[busca]['gols']):
            print(f"Jogo {i+1}: {v} gols.")
        print("="*50)
print("Obrigado, volte sempre!!")







