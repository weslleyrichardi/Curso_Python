from datetime import date
jovem = 0
maior_idade = 0
atual = date.today().year
for pessoa in range(1, 8):
    nascimento= int(input(f"Em que ano a {pessoa}° pessoa nasceu?: "))
    idade = atual - nascimento
    
    if idade >= 21:
        maior_idade += 1
    else:
        jovem += 1
print (f'Temos {jovem} jovens, e {maior_idade} maiores de idade')