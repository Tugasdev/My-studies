a=int(input("digite o comprimento do \033[7;35;44mprimeiro lado\033[0;37;40m\n"))
b=int(input("digite o comprimento do segundo lado\n"))
c=int(input("digite o comprimento do terceiro lado\n"))

if a + b > c and b + c > a and a + c > b:
    print ("é possivel fazer um triangulo com esses comprimentos.")
else:
    print ("não é possivel fazer um triangulo com esses comprimentos.")