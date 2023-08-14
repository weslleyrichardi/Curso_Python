brasileirao = ('Corintias', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
               'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Bota Fogo',
               'Atlético-PA', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
               'EC Vitória', 'Coritiba', 'Avai', 'Ponte Preta', 'Atlético GO')

#Questão A:
print("\n Os primeiros cinco times são são:")
print("—"*40)
for Lugar, Time in enumerate(brasileirao[:5]):
    print(f"|  {Lugar+1}° : {Time}")
print("—"*40)
#Questão B:
print(" Os últimos quatro times foram:")
print("—"*40)
for Lugar, Time in enumerate(brasileirao[-4:]):
    print(f"|  {Lugar+1}° : {Time}")
print("—"*40)
#Questão C:
print(" Times em ordem alfabética:")
print("—"*40)
for Time in sorted(brasileirao):
    print(Time)
print("—"*40)
#Questão D:
print(" Localização da Chapecoense:")
print("—"*40)
print(f" O time da chepecoese esta localizado naposição: {brasileirao.index('Chapecoense')+1}\nse começar do um")
