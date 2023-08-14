def leiaInt(MSG):
    ok = False
    valor = 0
    while True:
        n = str(input(MSG))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mERROR: "{n}" não é um número inteiro.\033[m')
        if ok:
            break
    return valor

  
n = leiaInt("Digite um número: ")
print(f"O valor digitado foi {n}")
