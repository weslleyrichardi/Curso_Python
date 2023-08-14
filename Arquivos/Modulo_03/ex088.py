# Biblioteca
from random import randint
# Entrada de dados

quant = int(input("Quantos jogos serão dortesdos?: "))
# Variáveis, listas, contadore e etcetera.
temporarios = list()
jogo = list()
numero = vezes = 0
# Sorteio e análises
while vezes < quant:
    palpites = 0
    while True:
        numero = randint(1, 60)
        if numero not in temporarios:
            temporarios.append(numero)
            palpites += 1
        if palpites >= 6:
            break
    jogo.append(temporarios[:])
    temporarios.clear()
    vezes += 1
# Saída de dados
print("="*30)
for indice, lista in enumerate(jogo):
    print(f"Jogo {indice+1:<2}: {lista}")
