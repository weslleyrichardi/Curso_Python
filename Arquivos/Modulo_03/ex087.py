matriz = ([0]*3, [0]*3, [0]*3)
soma = soma2 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input("Digite um número: "))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 2:
            soma2 += matriz[l][2]
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^2}]", end="")
    print()
print(f"A soma dos valores pares digitados é: {soma}.")
print(f"A soma dos valores da 3° coluna é: {soma2}")
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print(f"Maior número da segunda linha é o {maior}")



