num1 = int(input("\nDigite o 1° número: "))
num2 = int(input("Digite o 2° número: "))

opção = 0
while opção != 5:
    
    opção = int(input(
    '''
    O que deseja realizar?
|—————————————————————————————|
|          |                  |
|[1] Somar | [2] Multiplicar  |
|[3] Maior | [4] Novos numeros|
|                             |
|\033[31m[5] Sair do programa.        \033[m|
|—————————————————————————————|
 Digite o número da sua opção: '''))
    print('\n')
    
# PRIMEIRA OPÇÃO
    if opção == 1:
        soma = num1 + num2
        print(f'  O resultado da soma entre {num1} + {num2} é {soma}')

# SEGUNDA OPÇÃO
    elif opção == 2:
        multiplicacao = num1 * num2
        print(f'  O resultado da multiplicação entre {num1} × {num2} é {multiplicacao}')
        
# TERCEIRA OPÇÃO
    elif opção == 3:
        if num1 > num2:
            print('  O primeiro número é maior.')
        elif num2 > num1:
            print('  O segundo número é maior.')
        else:
            print('  Os dois são iguais.')
    
# QUARTA OPÇÃO
    elif opção == 4:
        print("Digite novamente.")
        num1 = int(input("Digite o 1° número: "))
        num2 = int(input("Digite o 2° número: "))
       
# QUINTA OPÇÃO
    elif opção == 5:
        print('Programa finalizando.')
        
# OPÇÃO INVÁLIDA
    else:
        print("Opção invalida, tente novamente.")
        
# CORTE PARA PRÓXIMA OPÇÃO 
    print('\033[36m', '—'*35, '\033[m')
    
# FIM DA EXECUÇÃO
print('Obrigado e volte sempre. :D')


