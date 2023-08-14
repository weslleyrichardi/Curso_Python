import ex107
real = float(input(" Qual o valor? "))
print(f" A metade de R${real} é R${ex107.metade(real)}")
print(f" O dobro de R${real} é R${ex107.dobro(real)}")
print(f" Com o aumento de 17% em R${real} reais é R${ex107.aumentar(real, 17)}")
print(f" Com a redução de 28% em R${real} reais é R${ex107.diminuir(real, 28)}")

