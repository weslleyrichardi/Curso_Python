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


def leiafloat(MSG):
    while True:
        try:
            num = float(input(MSG))
        except (ValueError, TypeError):
            print(f'\033[0;31mERROR: Não é um número real.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[0;31mERROR: O usuário decidiu não digitar nada.\033[m')
            return 0
        else:
            return num


num1 = leiaint("Digite um número: ")
num2 = leiafloat("Agora digite um número real: ")
print(f"Os valores digitados foram {num1} e {num2}")
