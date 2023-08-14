pessoa = dict()
pessoas = list()
mulheres = list()
soma = 0


while True:
    pessoa.clear
    pessoa["Nome"] = str(input("Nome: ")).strip()
    while True:
        pessoa["Sexo"] = str(input("Sexo [M/F]: ")).upper()[0]
        if pessoa["Sexo"] in 'MF':
            break
        print("\033[31mERRO!\033[m Porfavor digite \033[32mM\033[m ou \033[32mF\033[m")
    pessoa["Idade"] = int(input("idade: "))
    soma += pessoa["Idade"]
    pessoas.append(pessoa.copy())
    if pessoa["Sexo"] in 'Ff':
        mulheres.append(pessoas.copy())
    while True:
        resp = str(input("Deseja continuar? [S/N]: ")).upper()[0]
        if resp in 'SN':
            break
        print("\033[31mERRO!\033[m Porfavor digite \033[32mS\033[m ou \033[32mFN\033[m")
    if resp in 'N':
        break

print("="*30)
print(f"{len(pessoas)} pessoas foram cadastradas")
print("="*30)
media = soma / len(pessoas)
print(f"A média das idades é {media:.1f}")
print("="*30)
print("As mulheres cadastradas foram: ", end='')
for pessoa in pessoas:
    if pessoa['Sexo'] == 'F':
        print(f"{pessoa['Nome']}", end=" - ")
print()
print("="*30)
print("Pessoas com a idade a cima da média: ",end="")
for pessoa in pessoas:
    if pessoa["Idade"] > media:
        print("    ")
        for k, v in pessoa.items():
            print(f"{k}: {v}\n", end="")
print("="*30)
