print("="*41)
solicitacao = int(input("Quanto deseja sacar? R$"))
print("="*41)
saque = solicitacao
cedula = 50
total_ced = 0
while True:
    if saque >= cedula:
        saque -= cedula 
        total_ced += 1
    else:
        if total_ced > 0:
            print(f"Sacou {total_ced} de \033[32mR${cedula}\033[m")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_ced = 0
        if saque == 0:
            break
print(f"Você sacou \033[32mR${solicitacao:.2f}\033[m")