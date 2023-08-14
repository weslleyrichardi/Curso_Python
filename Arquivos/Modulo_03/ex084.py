#Listas e variáveis.
temporario = []
principal = []
maior = menor = 0
#Entrada de dados.
while True:
    temporario.append(str(input("Nome: ")))
    temporario.append(float(input("Peso: ")))
    if len(principal) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    resp = str(input("Deseja continuar? [S/N]: "))
    if resp in "Nn":
        break
print("—"*40)
#Saída de dados.
print(f"Foram cadastradas {len(principal)} pessoas.")
print(f"O maior peso foi {maior:.1f}kg de: ", end=" ")
for pessoa in principal:
    if pessoa[1] == maior:
        print(pessoa[0], end=", ")
    if pessoa == pessoa[-1]:
        print("\n")
print(f"\nO menor peso foi {menor:.1f}kg de: ", end=" ")
for pessoa in principal:
    if pessoa[1] == menor:
        print(pessoa[0], end=", ")
