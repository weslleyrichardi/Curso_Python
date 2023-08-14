palavras = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON",
	           "CURSO", "GRATIS", "ESTUDAR", "PRATICAR",
	           "TRABALHAR", "MERCADO", "PROGRAMADOR", "FUTURO")
print("_"*40)
for palavra in palavras:
    print(f"\nEm {palavra} temos:", end=' ')
    for Letra in palavra:
        if Letra.lower() in 'aeiou':
            print(Letra, end='-')
print("\n")
print("—"*40)

