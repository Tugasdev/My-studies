numero = input ("digite um numero de 0 a 9999\n")
if len(numero)==1:
    print ("seu numero:\ntem {} unidades.".format (numero[0]))
elif len(numero)==2:
    print ("seu numero tem:\n{} unidades\n{} dezenas.".format (numero[1], numero[0]))
elif len(numero)==3:
    print ("seu numero tem:\n{} unidades\n{} dezenas\n{} centenas".format (numero[2], numero[1], numero[0]))
elif len(numero)==4:
    print ("seu numero tem:\n{} unidades\n{} dezenas\n{} centenas\n{} milhares.".format (numero[3], numero[2], numero[1], numero[0]))
else:
    print ("não é um numero válido")