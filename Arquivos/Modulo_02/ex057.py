'''Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores ‘M’ ou ‘F’. Caso esteja
errado, peça a digitação novamente até ter um valor
correto'''
sexo = input('Qual é o seu sexo [M/N]: ').strip()[0]
while sexo not in 'MmFf':
    sexo = input('\033[31mOperação inválida.\033[m Digite seu sexo \033[32mcorretamente\033[m [M/F]: ').strip()[0]
print('Sexo registrado com \033[32msucesso\033[m!!')