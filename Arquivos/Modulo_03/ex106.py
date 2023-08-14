color = ("\033[m",           #NORMAL
	        "\033[0;30;41m",    #VERMELHO
	        "\033[0;30;42m",    #VERDE
	        "\033[0;30;43m",    #AMARELO
	        "\033[0;30;44m",    #AZUL
	        "\033[0;31;47m",       #BRANCO
	       )
	        
	        
def titulo(msg, cor = 0):
    tam = len(msg)+4
    print(color[cor], end='')
    print("~"*tam)
    print(f"  {msg}  ")
    print("~"*tam)
    print(color[0], end='')
    
    
def ajuda(cmd):
    titulo(f'Acessando as informações do programa {cmd}', 5)
    print(color[5], end='')
    help(cmd)
    print(color[0], end='')
    
    

while True:
    titulo("INTERACTIVE HELP", 3)
    cmd = str(input("HELP >>> "))
    if cmd.upper() == "FIM":
        break
    else:
        ajuda(cmd)
        
titulo("FIM DO PROGRAMA, ATÉ A PRÓXIMA!", 2)

