
nome_mais_velho = 0
mais_velho = 0
soma_das_idades = 0
mulheres = 0
for n in range(1, 5):
    print(f'——————{n}° Pessoa——————')
    nome = str(input(f'Nome: ')).strip().capitalize()
    idade = int(input(f'Idade de {nome}?: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    
    if n == 1 and sexo in "Mm":
        mais_velho = idade
        nome_mais_velho = nome
    else:
        if idade > mais_velho and sexo in "Mm":
            maisvelho = idade
            nome_mais_velho = nome
    if idade < 20 and sexo in "Ff":
        mulheres += 1
    soma_das_idades += idade

media = soma_das_idades / n

print(f'''
A media das idades é {media}.
O homem mais velho é {nome_mais_velho} e sua idade é de {mais_velho} anos.
E temos {mulheres} mulheres com menos de 20 anos.
''')

