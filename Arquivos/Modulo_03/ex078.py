valores = [0]*5
maior = menor = 0
print("—"*23)
for posicao in range(0, 5):
    valores[posicao] = int(input(f"Digite um valor → {'|':>1}"))
print("—"*35)
print(f"Os valores foram {valores}")
print("—"*35)
print(f"O menor valor foi {min(valores)} e se encontra na posição ", end='')
for posi, valor in enumerate(valores):
    if valor == min(valores):
        print(posi+1, end="... ")
print("\t")
print(f"O maior valor foi {max(valores)} e se encontra na posição ", end='')
for posi, valor in enumerate(valores):
    if valor == max(valores):
        print(posi+1, end = "... ")
