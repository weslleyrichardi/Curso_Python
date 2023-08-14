N = int(input("Onde ira parar a sequência de Fibonacci?: "))
a = 0
b = 1
c = 1
cont = 0
print(F"\n{'—'*43}")
while cont < N:
    if cont == 0:
        c = 0
    print(f'{c} ', end='⟩ ')
    a = a + b
    b = c
    c = a
    cont += 1
print(F"\n{'—'*19}»FIM«{'—'*19}")
