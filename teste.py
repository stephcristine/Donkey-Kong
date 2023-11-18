import os
import WConio2 as WConio2
import cursor

os.system('cls')
cursor.hide()

voce = "$"  #personagem
voceI = 2   #linha
voceJ = 15  #coluna

teste = "*"  #personagem
testeI = 8   #linha
testeJ = 8  #coluna

teste2 = 0

simbolo = ''

contador = 0 #controla a velocidade de movimentos

while(simbolo != 'o'):
    #posicionar o cursor no começo da tela
    WConio2.gotoxy(0,0)
    if voceI > 0 and contador % 600 == 0:
      voceI += 1

    if voceI > 10:
        voceI = 1


    print('*' * 25)  #linha de cima
    for i in range(10): #10 linhas
        
        print('*', end='')  #abre cada linha

        for j in range(23): #23 colunas
           
            if i==voceI and j==voceJ:
                print(voce, end='')
                if voceI==testeI and voceJ==testeJ:
                    teste = " "
                    teste2 +=1
            elif i==testeI and j==testeJ:
                print(teste, end='')
            else:
                 print(' ', end='')
        
        print('*')  #fecha cada linha 

    print('*' * 25) #linha de baixo
    print(teste2)
    print(voceJ)
    print(voceI)

    contador += 1

    #pegar interações do usuario
    if WConio2.kbhit():
        (tecla, simbolo) = WConio2.getch()
        
        if simbolo=='a' or simbolo=='A':
            voceJ -= 1
        elif simbolo=='d' or simbolo=='D':
            voceJ += 1
        elif simbolo=='w' or simbolo=='':
            voceI -= 1

print("Fim do Jogo!")