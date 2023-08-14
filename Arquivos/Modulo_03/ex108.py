import ex108
real = float(input(" Qual o valor? "))
print(f" A metade de {ex108.moeda(real)} é {ex108.moeda(ex108.metade(real))}")
print(f" O dobro de {ex108.moeda(real)} é {ex108.moeda(ex108.dobro(real))}")
print(f" Com o aumento de 17% em {ex108.moeda(real)} reais é {ex108.moeda(ex108.aumentar(real, 17))}")
print(f" Com a redução de 28% em {ex108.moeda(real)} reais é {ex108.moeda(ex108.diminuir(real, 28))}")

