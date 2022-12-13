tax=int(input("Quantos km viajou?\n"))
if tax <=200:
    print ("O preço da corrida ficou por R${}.".format(tax*0.50))
else:
    print ("O preço da viagem ficou por R${}.".format(tax*0.45))