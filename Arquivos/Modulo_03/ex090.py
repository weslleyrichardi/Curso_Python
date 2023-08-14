boletim = dict()
boletim["nome"] = str(input("Nome do aluno(a): "))
boletim["media"] = float(input("Média do aluno(a): "))
boletim["final"] = ""

if boletim["media"] >= 6:
    boletim["final"] = "Aprovado"
else:
    boletim["final"] = "Recuperação"
print("_"*41)
print(f"|{'Nome:':<14}|{'Média:':<9}|{'Estado:':<15}|")
print(f"|{boletim['nome']:.<14}|{boletim['media']:.<9.1f}|{boletim['final']:.<15}|")	