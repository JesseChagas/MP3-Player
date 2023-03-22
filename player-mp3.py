from pygame import mixer
from PySimpleGUI import PySimpleGUI as sg

def tocar_musica(nome_musica):
    mixer.init() # Iniciador do mixer do Pygame
    mixer.music.load(nome_musica) # Comando que carrega a música recebida pelo input
    mixer.music.play() # Comando que toca a música que foi recebida pelo input
    print(f'Está tocando {nome_musica}... Aproveite') # Comando que mostra a música que está tocando

sg.theme('DarkPurple1') # Definição do tema da interface do programa

layout = [
    [sg.Text('MP3 PLAYER'.center(50), font='Consolas')], # Título do programa
    [sg.Text('NOME DA MÚSICA:', font='Consolas'), sg.Input(key='music', size=(42, 1))], # Input da música que será tocada
    [sg.Button('Selecionar', size=(25, 1)), sg.Button('Tocar', size=(25, 1))], # Botão para selecionar a música e botão para tocar a música
    [sg.Text('', size=(55, 1), key='tocando')] # Campo para exibir qual música está sendo tocada
]

janela = sg.Window('Mp3 player', layout) # Criação da janela

print('Bem-vindo ao Mp3 player!')

while True:
    eventos, valores = janela.read()

    if eventos == sg.WIN_CLOSED:
        break
    
    if eventos == 'Selecionar':
        try:
            musica = open(valores['music'])
            janela['tocando'].update(valores['music'])
        except:
            sg.popup('Erro! :/')
    
    if eventos == 'Tocar':
        tocar_musica(valores['music'])
    
janela.close()
mixer.quit() # Encerra o mixer do Pygame
