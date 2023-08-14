mais_de18 = homens = menos_de20 = 0
print("—"*25)
while True:
    sexo = input("Sexo [H/M]: ").upper()[0]
    idade = int(input("Idade: "))
    if idade > 18:
        mais_de18 += 1
    if sexo == "H":
        homens += 1
    if sexo == "M" and idade < 20:
        menos_de20 += 1
    parar = input("Deseja parar? [S/N]: ").upper()
    print("—"*25)
    if parar == "S":
        break
print(f"""
Foram cadastradas {mais_de18} pessoas com mais de 18 anos.
{homens} homens e {menos_de20} mulheres com menos de 20 anos.
""")
