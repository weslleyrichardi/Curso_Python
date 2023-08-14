valores = list()
while True:
    valores.append(int(input("Dugute um número: ")))
    parada = input("Deseja continuar? [S/N] ")
    if parada in "Nn":
        break
print("_"*40)

print(f"Foram digitados {len(valores)} valores.")
valores.sort(reverse=True)
print(f"A lista em números decrescente é {valores}")
print(f"O número 5 foi digitado. Sua primeira ocorrência foi na posição {valores.index(5)}" if 5 in valores else "O número 5 não teve ocorrência na lista.")
