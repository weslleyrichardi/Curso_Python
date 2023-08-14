temp = 0
valores = [[], []]
for posi in range(0, 7):
    temp = int(input("Digite um número: "))
    if temp[posi] % 2 == 0:
        valores[0].append(temp[posi])
    elif temp[posi] % 2 == 1:
        valores[1].append(temp[posi])
valores[0].sort()
print(f"Os valores pares são: {valores[0]}")
valores[1].sort()
print(f"Os valores impares são: {valores[1]}")

