from random import randint


while True:
    roll = input("Digite 'Ok' para rolar os dados ou qualquer tecla para sair: ")
    if(roll.upper() == 'OK'):
        print("O dado caiu no número: %d" %(randint(1, 6)))
    else:
        break
