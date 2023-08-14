quantidade = int(input("Quantos termos: "))
termo = int(input("Primeiro termo: "))
razão = int(input("Razão da PA: "))

contador = 1
Parar = False

while not Parar and contador <= quantidade:
    print(f"{contador}° termo: {termo}")
    termo += razão
    contador += 1
    if contador > quantidade:
        mais = int(input("quantos termos deseja adicionar?: "))
        quantidade += mais
        if quantidade == 0:
            Parar = True