salario=float(input("digite o valor do salário\nR$"))
if salario>=1250:
    aumento = salario/10
    salario = salario + aumento
    print (f"o valor do salário ajustado é de {salario}, tendo um aumento de R${aumento}0.")
else:
    aumento = salario/100*15
    salario = salario + aumento
    print (f"o valor do salário ajustado é de {salario}, tendo um aumento de R${aumento}0.")