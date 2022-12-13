import random

escolha = random.randint(1,5)

numero = int(input ("tente adivinhar o numero q escolhi! (entre 1 e 5)\n"))
print (f"eu escolhi {escolha}, isso quer dizer que...")

if escolha == numero:
    print ("parabéns, você acertou!")
else:
    print("você errou :/")