numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'dose', 'treze', 'quatorze', 'quinze', 'desesseis', 'desessete', 'desoito', 'desenove', 'vinte')
check = 0
while check == 0:
    digit = int (input ("Digite um numero de 0 a 20, ou digite qualquer outro numero pra sair: "))
    if digit > 20:
        check =+1
    else:
        print (numeros [digit])