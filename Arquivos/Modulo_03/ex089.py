lista_1 = list()
print("="*30)
while True:
    media = 0
    nome = str(input("Digite o nome do aluno: "))
    nota1 = float(input("Digite a nota um do aluno: "))
    nota2 = float(input("Digite a nota dois do aluno: "))
    media = (nota1 + nota2) / 2
    lista_1.append([nome, nota1, nota2, media])
    print("="*30)
    resp = str(input("Continuar? [S/N] »»» \033[m"))
    print("="*30)
    if resp in ("Nn "):
        break
print(f"{'Número':<10}:{'Média':<10}:{'Nome:':<10}")
for lista in range (0, len(lista_1)):
    	print(f"{lista+1:<9} | ", end='')
    	print(f"\033[32m{lista_1[lista][3]:<8}\033[m |" if lista_1[lista][3] >= 6 else f"\033[31m{lista_1[lista][3]:<8} \033[m|", end='')
    	print(f"{lista_1[lista][0]:<15}")
"""________________________________________________________________________________________________"""
codigo = 0
while True:
    print("="*30)
    print("\nDigite 999 para finalizar a sessão.")
    codigo = int(input("Digite o Número do aluno para mais informações: "))
    if codigo == 999:
        break
    print(f"Nome: {lista_1[codigo-1][0]}")
    if lista_1[codigo-1][1] >= 6:
        print(f"Nota 1: \033[32m{lista_1[codigo-1][1]}\033[m")
    else:
        print(f"Nota 1: \033[31m{lista_1[codigo-1][1]}\033[m")
    if lista_1[codigo-1][2] >= 6:
        print(f"Nota 2: \033[32m{lista_1[codigo-1][2]}\033[m")
    else:
        print(f"Nota 2: \033[31m{lista_1[codigo-1][2]}\033[m")
    if lista_1[codigo-1][3] >= 6:
        print(f"Média final: \033[32m{lista_1[codigo-1][3]}\033[m")
    else:
        print(f"Média final: \033[31m{lista_1[codigo-1][3]}\033[m")
"""________________________________________________________________________________________________"""
print("="*30)
print("Obrigado volte sempre.")