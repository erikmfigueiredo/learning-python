#JOGO NIM

# OBS:
# n = número de peças iniciais;
# m = número maximo de peças que pode retirar por jogada;
# Para ganhar consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador.
# Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.

def computador_escolhe_jogada(n,m):
    cont=m
    while m<=n:
        if float(((n-cont)%(m+1)))==0:
            return(cont)
        cont=cont-1
    if m>n:
        return(n)

def usuario_escolhe_jogada(n,m):
    i=1
    while i!=0:
        retira = int(input("\nQuantas peças você vai tirar? "))
        if retira<=m and retira>0:
            return(retira)
        else:
            print("\nOops! Jogada inválida! Tente de novo.")
            i=1

# Se inicio=1 é a vez do usuário
# Se inicio=0 é a vez do computador
# Se vencedor=1 o ganhador é o usuário
# Se vencedor=0 o ganhador é o computador

def partida():

    n = int(input("\nQuantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n%(m+1)==0:
       print("\nVocê começa!")
       inicio=1;
    else:
        print("\nComputador começa!")
        inicio=0;

    while n!=0:
        if inicio==1:
            x=usuario_escolhe_jogada(n,m)
            print("Voce tirou",x,"peças.")
            n = n-x
            print("Agora resta apenas",n,"peça no tabuleiro.")
            inicio=0
            vencedor=1

        if inicio==0:
            y=computador_escolhe_jogada(n,m)
            print("\nO computador tirou",y,"peça.")
            n = n-y
            print("Agora resta apenas",n,"peça no tabuleiro.")
            inicio=1
            vencedor=0

    if n==0:
        if vencedor==0:
            print("Fim do jogo! O computador ganhou!")
            return (0)
    
        else:
            print("Fim do jogo! Você ganhou!")
            return (1)


def campeonato():
    computador = 0
    voce = 0
    x=1

    while x<=3:
        print("\n**** Rodada",x,"****")
        y=partida()
        x=x+1
        if y==0:
            computador = computador+1
        if y==1:
            voce = voce+1
    print("\n**** Final do campeonato! ****")
    print("\nPlacar: Você",voce,"X",computador,"Computador")
    

print("Bem-vindo ao jogo do NIM! Escolha:\n\n")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
escolhe = int(input())
if escolhe==1:
    print("Voce escolheu uma partida isolada")
    partida()
if escolhe==2:
    print("Voce escolheu um campeonato!")
    campeonato()
