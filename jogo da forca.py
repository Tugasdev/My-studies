import random

with open('C:\\Estudos de Python\\animais.txt', 'r', encoding='utf-8') as arquivo:
  nomes = []
  for linha in arquivo:
    nomes.append(linha.strip())

for i, item in enumerate (nomes):
    if item == '-':
        nomes = [i]


def acerto(letra, palavra_certa, palavra_escondida):
    palavra_nova = []
    for i in range(len(palavra_certa)):
        if palavra_escondida[i] == '_':
            if palavra_certa[i] == ' ':
                palavra_nova.append(' ')
            elif palavra_certa[i] == letra:
                palavra_nova.append(letra)
            else:
                palavra_nova.append('_')
        else:
            palavra_nova.append(palavra_escondida[i])
    return ''.join(palavra_nova)

escolha = random.choice (nomes)
escolha = escolha.lower()
palavra_certa = escolha
palavra_escondida = '_' * len(palavra_certa)

print(f'''
Bem vindo ao jogo da forca!!
Você tem que adivinhar a palavra de um animal!
O animal tem {len(escolha)} letras!
Vamos começar. Você tem 10 chances.
{('_'*len(escolha))}
''')

tentativas = 0
letras_tentadas = []

while '_' in palavra_escondida and tentativas < 10:
    letra = input(f'Digite uma letra! (letras já usadas: {letras_tentadas})\n')

    palavra_escondida = acerto(letra, palavra_certa, palavra_escondida)

    if letra in letras_tentadas:
        print ('Você já tentou essa letra. Tente de novo.')

    elif letra not in palavra_escondida:
        tentativas = tentativas + 1
        letras_tentadas.append(letra)

    else:
        letras_tentadas.append(letra)

    print(f'{palavra_escondida}         --Tentativa numero {tentativas}--')

if tentativas == 10:
    print (f"Você perdeu :/ a palavra era {escolha}")

else: 
    print ("Ebaaaa conseguiu!!")

input ('\n\nPressione qualquer tecla para fechar.')
