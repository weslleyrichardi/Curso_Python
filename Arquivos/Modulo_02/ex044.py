print('='*10, 'Loja WS o Silva', '='*10)

preco = int(input('\nQuanto custa o produto? \033[1;32mR$'))
tipo = int(input('''\033[mFORMA DE PAGAMENTO
__________________________________
|                                |
| [ 1 ] Á vista dinheiro/Cheque. |
| [ 2 ] Á vista no cartão.       |
| [ 3 ] Em até 2x no cartão.     |
| [ 4 ] Em 3x ou mais no cartão. |
|________________________________|

Qual é a opção?: '''))

if tipo == 1:
    preco_final = preco - (preco * 10/100)
    print(f'Desconto de \033[1;35m10%\033[m.\nAgora seu produto custa \033[1;32mR${preco_final:.2f}\033[m')
elif tipo == 2:
    preco_final = preco - (preco * 5/100)
    print(f'\nDesconto de \033[1;35m5%\033[m\nAgora seu produto custa \033[1;32mR${preco_final:.2f}\033[m')
elif tipo == 3:
    preco_final = preco / 2
    print(f'\nAgora você vai pagar em 2x de \033[1;32mR${preco_final:.2f}\033[m')
elif tipo == 4:
    vezes = int(input('Em quantas vezes?: x'))
    preco_final1 = (preco + (preco * 20/100))/vezes
    preco_final2 = preco + (preco * 20/100)
    print(f'''\nParcelando agora você deve pagar em {vezes}x de \033[1;32mR${preco_final1:.2f}\033[m com juros de \033[1;35m20%\033[m
Agora seu produto custa \033[1;32mR${preco_final2:.2f}\033[m''')
else:
    print('\033[1;31;3m Opção invalida! Tente novamente. \033[m')

