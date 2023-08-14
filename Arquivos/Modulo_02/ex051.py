#10 Termos de uma P.A.
print(f'''
{"="*35}
   |   PROGRESSÃO ARITMÉTICA   |
{"="*35}
''')

termo = int(input('Primeiro termo: '))
razao = int(input('Qual é a Razão: '))

decimo = termo + (10 - 1) * razao

for TERMO in range(termo, decimo + razao, razao):
    print(f'{TERMO}', end=(' >> '))

print(f'Acabou')