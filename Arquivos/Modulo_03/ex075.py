nuns = (int(input("Digite um número: ")),
	       int(input("Digite outro um número: ")),
	       int(input("Digite mais um número: ")),
	       int(input("Digite o último número: ")))
print("—"*30)
if 9 in nuns:
    print(f"O ( 9 ) apareceu {nuns.count(9)} vezes")
else:
    print("O número ( 9 ) não foi digitado.")
if 3 in nuns:
    print(f"O primeiro ( 3 ) à aparecer está na posição {nuns.index(3)+1}")

else:
    print("O número ( 3 ) não foi digitado")
print(f"Os números pares digitados foram: ", end= " ")
for numero in nuns:   
    if numero % 2 == 0:
        print(numero)
print("\nAcabou")