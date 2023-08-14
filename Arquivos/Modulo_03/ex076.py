produtos_precos = ("Lápis", 1.75,
	                  "Borracha", 2.00,
                   "Caderno", 15.90,
                   "Estojo", 25.00,
                   "Transferidor", 4.20,
                   "Compasso", 9.99,
                   "Mochila", 120.32, 
                   "Canetas", 22.30,
                   "Livro", 34.90)
print(f'|{"—"*39}|')
print(f'|{"PRODUTOS DO WILLY":^39}|')
print(f'|{"—"*39}|')
for Produto in range(0, len(produtos_precos)):
    if Produto % 2 == 0:
        print(f'|{produtos_precos[Produto]:.<30}', end="")
    else:
        print(f'R${produtos_precos[Produto]:>7.2f}|')
print(f'|{"—"*39}|')