soma = 0
cont = 0
for c in range(0, 6):
    num = int(input(f'Digite o {c+1}° número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'\nDigitados {cont} números pares.\nA soma de todos os números pares é: {soma}')