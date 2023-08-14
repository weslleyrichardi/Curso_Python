lista_1 = []
lista_2 = []
lista_3 = []
while True:
    lista_1.append(int(input("Digite um número: ")))
    parada = input("Deseja continuar?: ")
    print("—"*25)
    if parada in "Nn":
        break
for num in lista_1:
    if num % 2 == 0:
        lista_2.append(num)
    else:
        lista_3.append(num)
print(f"Todos os valores digitados: {sorted(lista_1)}")
print(f"Os pares são {sorted(lista_2)}")
print(f"Os ímpares são {sorted(lista_3)}")
