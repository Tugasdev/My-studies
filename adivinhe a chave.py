chave = {}
chave["Jops"] = "Penis8090"
chave["Tugas"] = "Penis9080"
senha = input ("Digite a senha: ").capitalize()
acertou = False
while acertou == False:
    if senha in chave:
        print (f"Acertou! a senha é {chave[senha]}\n")
        senha = input ("Digite a senha: ").capitalize()
    elif senha in chave.values():
        acertou = True
    else:
        senha = input ("Você errou a senha. \nDica: rei delas: ").capitalize()
print ("Parabens, conseguiu acesso.")