from random import randint


def game(num, score):
    while score > 0:
        print("Você tem %d vida(s)" %(score))
        palpite = int(input("\nDigite seu palpite (1-100): "))
        
        if palpite > num:
            print("\nVocê chutou acima do número mágico.")
            score -= 1
        elif palpite < num:
            print("\nVocê chutou abaixo do número mágico.")
            score -= 1
        else:
            print("\nParabéns, você ganhou!!!")
            print("Número mágico: %d" %(num))
            print("Fim de jogo!")
            break
    else:
        return print("\nVocê perdeu!\nFim de jogo!")
            

print("*** Iniciando jogo ***")

print("\nDigite a dificuldade:\
      \n# 1 - Fácil\
      \n# 2 - Médio\
      \n# 3 - Difícil")
dificuldade = int(input())

if dificuldade == 1:
    score = 10
elif dificuldade == 2:
    score = 5
elif dificuldade == 3:
    score = 3
    
game(randint(1, 100), score)