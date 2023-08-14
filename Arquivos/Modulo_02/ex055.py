maior_pesp = 0
menor_peso = 0

for pessoa in range(1, 6):
    peso_informado = float(input(f'Digite o peso da {pessoa}° pessoa: '))
    
    if pessoa == 1:
        maior_peso = peso_informado
        menor_peso = peso_informado
    
    else:
        if peso_informado > maior_peso:
            maior_peso = peso_informado
        if peso_informado < menor_peso:
            menor_peso = peso_informado
    
    
print(f'O menor peso é {menor_peso:.2f}kg e o maior peso é {maior_peso:.2f}kg.')
