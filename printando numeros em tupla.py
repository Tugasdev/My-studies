from random import randint
numeros = (randint (1,10), randint (1,10), randint (1,10), randint (1,10), randint (1,10))
numero_maior= 0
numero_menor= 10
print (numeros)

for i in numeros:
    if i > numero_maior:
        numero_maior = i
    if i < numero_menor:
        numero_menor = i

print (f"O numero maior é {numero_maior}, e o numero menor é {numero_menor}.")