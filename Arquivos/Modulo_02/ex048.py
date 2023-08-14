
vezes = 0
soma = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        vezes += 1
        soma += n
print(f'\nA soma entre os {vezes} múltiplos de 3 é: {soma}')
