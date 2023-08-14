total_gasto = mais_demil = mais_barato = nome_barato = cont = 0
print("—"*40)
while True:
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: R$"))
    cont += 1
    total_gasto += preco
    if preco > 1000:
        mais_demil += 1
    if cont == 1 or preco < mais_barato:
        mais_barato = preco
        nome_barato = nome
    parar = input("Deseja continuar? [S/N]: ").upper()[0]
    print("—"*40)
    if parar == "N":
        break
print(f"""
{"—"*25}»FIM«{"—"*25}
O total gasto é de R${total_gasto:.2f}.
Foram {mais_demil} produtos custando mais de mil reais.
O produto mais barato foi {nome_barato} que custou R${mais_barato:.2f}.
""")