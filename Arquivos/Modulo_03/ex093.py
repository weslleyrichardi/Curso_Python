gols = list()
jogador = dict()
nome = str(input("Nome: "))
partidas = int(input("Quantidade de partidas jogadas: "))
for partida in range(1, partidas+1):
    gols.append(int(input(f"Gols na partida {partida}: ")))
jogador = {'Nome':nome, 'Partidas':partidas, 'Lista de gols por partida': gols[:],'Gols': sum(gols)}
print("="*30)
print(jogador)
print("="*30)
for k, v in jogador.items():
    print(f"{k}: {v}")
print("="*30)
print(f" O jogador {jogador['Nome']} jogou {partidas} partidas")
for i, v in enumerate(gols):
    print(f"  - Jogo {i+1}: {v} gols")
print("="*30)

