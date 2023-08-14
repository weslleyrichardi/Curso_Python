from random import randint
numero = list()
def sorteia(x):
    for posi in range(0, 5):
        x.append(randint(1, 10))
    print("-"*30)
    print(x)
    print("-"*30)
def somaPar(x):
    soma = 0
    for valor in x:
        if valor % 2 == 0:
            soma += valor
    print("-"*30)
    print(f"{soma:^30}")
    print("-"*30)


sorteia(numero)
print()
somaPar(numero)
 