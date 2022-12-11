import random
tentativas = 0
dado = 0
while (dado <20):
    dado = random.randint (1,20)
    tentativas +=1
    print (dado)
print (f"foram {tentativas} roladas pra chegar ao 20")

