matriz = ([[0], [0], [0]], [[0], [0], [0]], [[0], [0], [0]])
for l in range(0, 3):
    for c in range(0, 3):
        matriz[c][l] = int(input("Digite um número: "))
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[c][l]:^5}]", end="")
    print()
