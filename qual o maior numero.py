num1=int(input("digite o primeiro numero\n"))
num2=int(input("digite o segund numero\n"))
num3=int(input("digite o terceiro numero\n"))

menor = num1
if num2<num3 and num2<num3:
    menor=num2
elif num3<num1 and num3<num2:
    menor=num3

maior = num1
if num2>num1 and num2>num3:
    maior=num2
elif num3>num1 and num3>num2:
    maior=num3

print (f"o maior numero é {maior}, e o menor numero é {menor}")