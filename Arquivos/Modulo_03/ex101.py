def voto(nascimento):
    from datetime import date
    atual = date.today().year
    idade = atual - nascimento
    if idade < 16:
        return f'Com {idade} anos o voto é Negado'
    elif 16 >= idade < 18 or idade > 65:
        return f'Com {idade} anos o voto é Opcional'
    else:
        return f'Com {idade} anos o voto é Obrigatório'


print(voto(int(input("Seu ano de nascimento: "))))
