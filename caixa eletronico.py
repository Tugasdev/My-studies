valor = int (input ("Digite o valor a ser sacado: R$"))
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0
while valor >= 50:
    valor -= 50
    nota50 += 1
while valor >= 20:
    valor -= 20
    nota20 +=1
while valor >= 10:
    valor -= 10
    nota10 +=1
while valor >= 1:
    valor -= 1
    nota1 += 1

print (f"Você receberá {nota50} notas de R$50, {nota20} notas de R$20, {nota10} notas de R$10 e {nota1} notas de R$1.")