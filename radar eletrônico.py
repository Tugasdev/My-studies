km=int(input("Quantos km por hora o carro foi?\n"))
if km>80:
    km=(km-80)*7
    print (f"a multa por estar acima do limite de velocidade é de R${km},00.")
else:
    print("ta tudo certo aqui, campeão.")