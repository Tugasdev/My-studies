frase=input ("digite uma frase\n")
frase=frase.lower()
print ("na frase tem:\n{} 'A'\naparece na primeira vez na posição {}\naparece pela ultima vez na posição {}".format (frase.count('a'), frase.find("a")+1, frase.rfind("a")+1))