import PySimpleGUI as sg

def tela_conversao():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Conversor de números', font=('Arial', 16))],
        [sg.Text('Digite um número inteiro: '), sg.Input(key='numero',size=(20))],
        [sg.Text('Escolha uma das bases para conversão')],
        [sg.Button('BINÁRIO'), sg.Button('OCTAL'), sg.Button('HEXADECIMAL')],
        [sg.Text('', key='resultado')]  
    ]

    janela = sg.Window('Conversor de números', layout)

    while True:
        evento, valores = janela.read()

        if evento == sg.WINDOW_CLOSED:
            break

        try:
            numero = int(valores['numero'])
            if evento == 'BINÁRIO':
                resultado = bin(numero)[2:]
            elif evento == 'OCTAL':
                resultado = oct(numero)[2:]
            elif evento == 'HEXADECIMAL':
                resultado = hex(numero)[2:]
            else:
                resultado = 'Opção inválida'

            janela['resultado'].update(f'Resultado: {resultado}')  # Atualiza o campo de resultado

        except ValueError:
            janela['resultado'].update('Digite um número válido')

    janela.close()

tela_conversao()
