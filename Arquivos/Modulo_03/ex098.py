from time import sleep
def contador(inicio, fim, passo):
    print("="*30)
    if passo == 0:
        p = 1
        print("Você gititou zero então alteramos para um")
    if passo < 0:
        passo *= -1
    print(f"Contador de {inicio} até {fim} de {passo} em {passo}.")
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=" → ", flush =True)
            sleep=(1)
            cont += 1
    
    if inicio == fim:
        print("Os valores \033[36mInicio\033[m e \033[36mPasse\033[m são iguais.")
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=" → ")
            sleep=(1)
            cont -= 1
    print("Fim")
    print("="*30)


contador(1, 10, 1)
contador(10, 1, 1)
contador(int(input("Inicio: ")), int(input("Fim: ")), int(input("Passo: ")))