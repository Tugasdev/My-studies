import PySimpleGUI as sg

sg.theme ('DarkAmber')

def faça_a_conta(numero1, operador, numero2):
  if operador == '*':
    resultado = numero1*numero2
    return resultado

  elif operador == '/':
    resultado = numero1/numero2
    return resultado

  elif operador == '+':
    resultado = numero1+numero2
    return resultado

  elif operador == '-':
    resultado = numero1-numero2
    return resultado

  else:
    resultado = 'resultado inexistente'
    return resultado
    

layout = [  [sg.Text('insane python calculator')],
            [sg.Text('digite uma conta')],
            [sg.InputText(size = (20,20), key = 'contak')],
            [sg.Button('FAÇA A CONTA'), sg.Button('Cancel')] ]

window = sg.Window('insane', layout)

while True:
    event, values = window.read()

    if event == 'FAÇA A CONTA':
        while True:
            try:
                conta = values['contak']
                conta = conta.split(' ')
                conta [0] = int(conta [0])
                conta [2] = int(conta [2])
        
            except:
                erritus = [[sg.Popup('Deu algum erro. Tente novamente.')]]
                erro_janela = sg.Window('Deu erro', erritus)
                erro_janela.read()

            else:
                resultado = faça_a_conta(conta[0], conta[1], conta[2])
                resultadinhos = [[sg.Text('o resultado é:')],
                                [sg.Popup(resultado)]]
                resultadinhos_janela = sg.Window('results', resultadinhos)
                resultadinhos_janela.read()

    elif event == sg.WIN_CLOSED or event == 'Cancel':
        break

      

window.close()