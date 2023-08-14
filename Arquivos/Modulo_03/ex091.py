from random import randint
from operator import itemgetter
from time import sleep
jogo = {"Jagador um": randint(1, 6),
        "Jogador dois": randint(1, 6),
        "Jogador três": randint(1, 6),
        "Jogador quatro": randint(1, 6)}
for k, v in jogo.items():
    print(f"{k:<14}: {v:>2}")
jogo = dict(sorted(jogo.items(), key=itemgetter(1), reverse=True))
print(">>>>>RANKING<<<<<")
cont = 0
for k, v in jogo.items():
    cont += 1
    if cont == 1:
        sleep(1)
        print("  Em 1° lugar...")
        sleep(2)
        print("  O vencedor foi...")
        sleep(3)
        print(f"  {k}: {v}")
    sleep(1)
    if cont >= 2:
        print(f"  {cont}° Lugar {k} : {v}")
    
