import random

jogar = "s"
jogadas = 0
while jogar == "s":
    pc = random.randint (1,10)
    jogada = input ("PAR OU IMPAR?? (P/I)\n")
    jogada.lower()
    valor = int (input ("MANDA O NUMERO\n"))
    valor += pc
    valor = valor % 2

    if jogada == "p":
        if valor  == 0:
            print ("Parabens, você ganhou! Vamos jogar de novo.\n")
        else:
            print ("Você perdeu :/")
            break

    elif jogada == "i":
        if valor == 1:
            print ("Parabens, você ganhou! Vamos jogar de novo.\n")
        else:
            print ("Você perdeu :/")
            break

    jogadas += 1

print (f"Você ganhou {jogadas} vezes seguidas!")