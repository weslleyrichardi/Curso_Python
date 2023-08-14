import random1
import time

#Escolhas
computador = random.randint(1, 3)
jogador = int(input('''\nSuas escolhas:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
qual é a sua escolha?: '''))


#Transformando para palavras.
if jogador == 1:
    jogador = 'Pedra'
elif jogador == 2:
    jogador = 'Papel'
elif jogador == 3:
    jogador = 'Tesoura'
else:
    jogador = 'Não jogou nada'
        
if computador == 1:
    computador = 'Pedra'
elif computador == 2:
    computador = 'Papel'
elif computador == 3:
    computador = 'Tesoura'

#Jo Ken po
print('\nJo')
time.sleep(1)
print('Ken')
time.sleep(1)
print('Po')

#Exibindo escolhas.
print(f'''
{"="*10}Escolhas{"="*10}|
Computador >> {computador}
 Jogador   >> {jogador}
{"="*28}|
''')

if jogador == computador:
    print('======>Impate<======|\nJogue novamente! :)\n===================|')
elif jogador == 'Pedra' and computador == 'Tesoura' or jogador == 'Papel' and computador == 'Pedra' or jogador == 'Tesoura' and computador == 'Papel':
    print('Jogador venceu!')
else:
    print('Computador venceu!')