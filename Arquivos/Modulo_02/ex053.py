frase = input("Digite uma frase: ").strip().upper().split()
juntu = ''.join(frase)
inverso = juntu[::-1]

if inverso == juntu:
    print(f'O inverso de {juntu} é {inverso}.\nA frase é um palíndromo!')

else:
    print(f'O inverso de {juntu} é {inverso}.\nA frase não é um palíndromo.')
