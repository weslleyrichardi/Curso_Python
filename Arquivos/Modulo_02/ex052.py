
num = int(input('Digite um número inteiro: '))
resultado = 0
for c in range(1, num+1):
    
    
    if num % c == 0:
        print(f'\033[32m{c}\033[m')
        resultado += 1
    else:
        print(f'\033[31m{c}\033[m')
        
if resultado == 2:
    print(f'\n Sim, {num} é um número primo.')
else:
    print(f'\n Não, {num} não é um número primo.')
