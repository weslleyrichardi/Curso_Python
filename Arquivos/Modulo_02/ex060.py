n = int(input('Escolha um número inteiro: '))
contador = n
fatorial = 1
print(f'O fatorial de {n}! = ', end="")
while contador > 0:
    print(f'{contador}', end='')
    if contador > 1:
        print(" × ", end="")
    else:
        print(" = ", end="")
    fatorial *= contador
    contador -= 1
print(fatorial)
