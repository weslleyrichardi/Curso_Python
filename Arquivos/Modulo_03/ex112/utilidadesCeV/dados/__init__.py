def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).strip().replace(",", ".")
        if entrada.isalpha() or entrada == "" or entrada.isalnum():
            print(f'\033[31mERROR!!! in "{entrada}"\033[m: Digite um valor monetário!!')
        else:
            valido = True
            return float(entrada)

