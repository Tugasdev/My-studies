nome = input ("digite um nome completo\n")
nome=nome.split()
print (len(nome))
print ("o primeiro nome é {} e o último é {}.".format(nome[0].title(), nome[-1].title()))