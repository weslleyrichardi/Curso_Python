def leiaint(MSG):
    while True:
        try:
            num = int(input(MSG))
        except (ValueError, TypeError):
            print(f'\033[31mERROR: Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[31mERROR: O usuário decidiu não digitar nada.\033[m')
            return 0
        else:
            return num


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc

