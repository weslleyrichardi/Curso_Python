import random

computador = random.randint(0, 10)
print('\nEu \033[34m(Computador)\033[m pensei em um número\nserá que você adivinha qual foi?')

jogador = int(input('Chute um número: '))
tentativas = 0
vencedor = False

while not vencedor:
    
    if jogador < computador:
        print('\033[33mMais...\033[m É um número maior.')
    elif jogador > computador:
        print('\033[33mMenos...\033[m É um número menor.')Jogador = int(input('Tentativa \033[31merrada\033[m, tente de novo: : ')   
    tentativas += 1
    if jogador == computador:
        vencedor = True

print(f"\nVocê \033[32macertou!!\033[m\nE tentou com {tentativas} tentativas.")