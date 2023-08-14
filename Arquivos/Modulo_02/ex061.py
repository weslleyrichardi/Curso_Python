termo = int(input("De onde começo a contar a PA: "))
razao = int(input("Qual sera o valor do salto: "))
contador = 1
while contador <= 10:
    print(f"{contador}° termo: {termo}")
    contador += 1
    termo += razao