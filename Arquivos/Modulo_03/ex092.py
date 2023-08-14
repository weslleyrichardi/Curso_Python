from datetime import datetime
cadastro = dict()
cadastro['Nome'] = str(input("Nome: ")).strip()
nasc = int(input("Ano de nascimento: "))
cadastro['Idade'] = datetime.now().year - nasc
cadastro['CTPS'] = int(input("Carteira de trabalho. (0) não tem: "))
if cadastro['CTPS'] != 0:
    cadastro['Contrato'] = int(input("Ano de contrato: "))
    cadastro['Salario'] = float(input("Salário: "))
    cadastro['Aposentadoria'] = cadastro['Idade'] + (cadastro['Contrato'] + 35) - datetime.now().year
print("="*30)
for k, v in cadastro.items():
    print(f"{k}: {v}")

