valores = list()
digito = 0
while True:
    digito = int(input("Digite um número: "))
    if digito not in valores:
        valores.append(digito)
    else:
        print("Valor duplicado, não vou adicionar.")
    parada = input("Deseja continuar? [S/N]: ")
    if parada in 'Nn':
        break 
print(f"\nOs digitados não duplicados foram: {sorted(valores)}")
