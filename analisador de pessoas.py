nome = ""
idade = 0
sexo = ""
mulheres_menores = 0
idadevelho = 0
nomevelho = ""
media = 0

for c in range (1, 5):
    print (f"----{c}º PESSOA----")
    nome = input ("Digite o nome da pessoa: ")
    idade = int (input ("Digite a idade da pessoa: "))
    sexo = input ("Digite o sexo da pessoa (H/M): ")
    sexo = sexo.lower()
    print ("\n")
    media = media + idade

    if sexo == "h" and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome

    if sexo == "m" and idade < 20:
        mulheres_menores = mulheres_menores + 1
media = media/4
print (f"\nA média de idade das pessoas é {media}\nO nome do homem mais velho é {nomevelho}, com {idadevelho} anos\nExistem {mulheres_menores} mulheres com menos de 20 anos.\n")