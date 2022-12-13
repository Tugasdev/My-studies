a=int(input("digite o comprimento do primeiro lado\n"))
b=int(input("digite o comprimento do segundo lado\n"))
c=int(input("digite o comprimento do terceiro lado\n"))

if a + b > c and b + c > a and a + c > b:
    print ("é possivel fazer um triangulo com esses comprimentos.")
else:
    print ("não é possivel fazer um triangulo com esses comprimentos.")