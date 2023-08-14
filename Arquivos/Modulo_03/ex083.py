expressao = str(input("Digite sua expressão: "))
parenteses = list()
for simbolo in expressao:
    if simbolo == "(":
        	parenteses.append("(")
    elif simbolo == ")":
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(")")
            break
if len(parenteses) == 0:
    print("Expressão válida.")
else:
    print("Expressão inválida.")
print("—"*30)
print(f"Expressão digitada: {expressao}")
        

