def ficha(nome = "<desconhecido>", gols = 0):
    print(f"O Jogador {nome} marcou {gols} gol(s).")


nome = str(input("Digite o nome do jogador: "))
gols = str(input(f"Quantos gols {nome} fez?: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == "":
    ficha(gols=gols)
else:
    ficha(nome, gols)
