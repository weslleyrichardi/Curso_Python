dupla = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Deis", "Onze", "Dose", "Treze", "Quatorze", "Quinze", "Deseceis", "Desecete", "Desoito", "Desenove", "Vinte")

while True:
    numero = int(input("Digite um número de 0 a 20: "))
    if 0 <= numero <= 20:
        break
    print("Tente novamente.")      
print(f"Número: {dupla[numero]}")

