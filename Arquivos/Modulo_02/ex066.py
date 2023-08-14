cont = soma = 0
while True:
    núm = int(input('Digite um número: '))
    if núm == 999:
        break
    cont += 1
    soma += núm
print(f'''
{"—"*25}
Você digitou {cont} números.
E a soma entre eles é {soma}.
{"—"*25}''')
